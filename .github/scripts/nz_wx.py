#!/usr/bin/env python3
"""新西兰行程 · 天气影响与决策（自动生成 wx.json）
数据源：MetService 官方 CAP 预警（alerts.metservice.com/cap/rss）+ Open-Meteo 16 天预报。
每天按当天走的路段和要做的事，把预警和预报翻译成「影响 + 决策」。
用法：python3 wx_live.py [输出路径]   默认 dist/nz/wx.json
同一份脚本被 GitHub Actions 每 3 小时跑一次（.github/scripts/nz_wx.py），所以只用标准库。"""
import json, re, sys, os, html, datetime, urllib.request, urllib.parse
from zoneinfo import ZoneInfo

NZ = ZoneInfo("Pacific/Auckland")
UA = {"User-Agent": "travel-nz-weather/1 (personal trip page)"}
CAP_RSS = "https://alerts.metservice.com/cap/rss"
SNOW = {71, 73, 75, 77, 85, 86}

# ---------- 每天：看哪的天气、走哪些路、做什么、备选 ----------
DAYS = [
 {"date": "2026-09-28", "place": "基督城", "lat": -43.489, "lon": 172.532, "areas": ["christchurch", "canterbury plains"],
  "arrive": True},
 {"date": "2026-09-29", "place": "库克山", "lat": -43.735, "lon": 170.096,
  "areas": ["canterbury high country", "canterbury plains", "mackenzie", "fairlie", "tekapo", "burkes"],
  "pass": "Burkes Pass · SH80", "pass_alt": "SH80 封了就住 Twizel 附近看 Tekapo、Pukaki，Mt Cook 挪到 9/30 早上（本来就是可选）",
  "hike": "Hooker Valley", "hike_alt": "改 Kea Point 1 小时，Hooker 挪到 9/30 早上",
  "sunset": "Peter's Lookout", "sunset_alt": "不等日落，直接去 Twizel 入住", "depart": "10:00 取车正好，别更早"},
 {"date": "2026-09-30", "place": "达尼丁", "lat": -45.912, "lon": 170.489,
  "areas": ["canterbury high country", "north otago", "otago", "dunedin", "waitati", "coastal"],
  "sunset": "Tunnel Beach", "sunset_alt": "Tunnel Beach 雨天很滑，别下去；在酒店门口的 St Clair 海滩看看天色就行"},
 {"date": "2026-10-01", "place": "蒂阿瑙", "lat": -45.414, "lon": 167.718,
  "areas": ["dunedin", "clutha", "southland", "gore", "lumsden", "fiordland", "catlins"],
  "sunset": "Te Anau 湖滨", "sunset_alt": "不用专门等，18:30 电话结束后看天色再说", "note": "18:00–18:30 房间里有电话，不受天气影响"},
 {"date": "2026-10-02", "place": "米尔福德峡湾", "lat": -44.672, "lon": 167.926,
  "areas": ["fiordland", "milford", "southland"], "milford": True,
  "sunset": "Manapouri Frasers Beach", "sunset_alt": "不去 Manapouri，回 Te Anau 休息"},
 {"date": "2026-10-03", "place": "瓦纳卡", "lat": -44.700, "lon": 169.135,
  "areas": ["southland", "queenstown", "central otago", "crown range", "otago lakes", "lakes district", "wanaka"],
  "pass": "Crown Range", "pass_alt": "Crown Range 封了走 SH6 经 Cromwell 到 Wanaka，多 30 分钟",
  "sunset": "That Wanaka Tree", "sunset_alt": "树就在湖边，小雨也能去，大雨就算了"},
 {"date": "2026-10-04", "place": "霍基蒂卡", "lat": -42.717, "lon": 170.966,
  "areas": ["queenstown", "lakes district", "haast", "westland", "west coast", "central otago"],
  "pass": "Haast Pass", "pass_alt": "Haast Pass 封了没有近路：等开，或在 Wanaka 多待半天再走", "westcoast": True,
  "sunset": "Hokitika 海滩", "sunset_alt": "海滩就在门口，下雨就在房间看"},
 {"date": "2026-10-05", "place": "亚瑟山口", "lat": -42.940, "lon": 171.562,
  "areas": ["westland", "west coast", "buller", "arthur", "porters", "canterbury high country", "canterbury plains", "christchurch"],
  "pass": "Arthur's Pass · Porters Pass", "pass_alt": "Arthur's Pass 封了走 Lewis Pass（SH7）回基督城，多 1.5 小时；17:00 前要还车，早点出发", "westcoast": True},
 {"date": "2026-10-06", "place": "罗托鲁瓦", "lat": -38.137, "lon": 176.251,
  "areas": ["auckland", "waikato", "bay of plenty", "rotorua", "waitomo"],
  "sunset": "Hannahs Bay 码头", "sunset_alt": "傍晚环湖跳过，改 Polynesian Spa 6:45 PM 湖景私汤（订票链接在行程页）"},
 {"date": "2026-10-07", "place": "霍比特人村", "lat": -37.857, "lon": 175.680,
  "areas": ["bay of plenty", "rotorua", "taupo", "waikato"], "outdoor": "Hobbiton 中文团照常，带雨衣"},
 {"date": "2026-10-08", "place": "奥克兰", "lat": -36.850, "lon": 174.763, "areas": ["waikato", "auckland"], "depart_home": True},
]
LEVEL = ["照常", "留意", "有备选", "改计划"]
ZH_WD = "一二三四五六日"

def get(url, timeout=40):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read().decode("utf-8", "ignore")

def tag(x, t):
    m = re.search(r"<%s>(.*?)</%s>" % (t, t), x, re.S)
    return html.unescape(m.group(1)).strip() if m else ""

def parse_dt(s):
    try: return datetime.datetime.fromisoformat(s.strip()).astimezone(NZ)
    except Exception: return None

def fmt_span(a, b):
    if not a: return ""
    def f(d): return "%d/%d %02d:%02d" % (d.month, d.day, d.hour, d.minute)
    if b and a.date() == b.date(): return f(a) + "–%02d:%02d" % (b.hour, b.minute)
    return f(a) + ("–" + f(b) if b else "")

def kind(c):
    if c is None: return ("", "cloud")
    if c == 0: return ("晴", "sun")
    if c <= 2: return ("晴间多云", "part")
    if c == 3: return ("阴", "cloud")
    if c <= 48: return ("雾", "fog")
    if c <= 57: return ("小雨", "rain")
    if c <= 65: return ("雨", "rain")
    if c <= 67: return ("冻雨", "rain")
    if c <= 77: return ("雪", "snow")
    if c <= 82: return ("阵雨", "rain")
    if c <= 86: return ("阵雪", "snow")
    return ("雷雨", "storm")

# ---------- 1. 官方预警 ----------
def fetch_alerts():
    out = []
    rss = get(CAP_RSS)
    for link in re.findall(r"<link>(.*?)</link>", rss, re.S)[1:]:
        link = link.strip()
        try: cap = get(link)
        except Exception: continue
        head = tag(cap, "headline"); area = tag(cap, "areaDesc"); desc = re.sub(r"\s+", " ", tag(cap, "description"))
        on, off = parse_dt(tag(cap, "onset")), parse_dt(tag(cap, "expires"))
        typ = ("road_snow" if "Road Snowfall" in head else "snow" if "Snow" in head else "rain" if "Rain" in head
               else "wind" if "Wind" in head else "thunder" if "Thunder" in head else "swell" if "Swell" in head else "other")
        lvl = "red" if "Red" in head else "orange" if "Orange" in head else "watch" if "Watch" in head else "road" if typ == "road_snow" else "info"
        out.append({"type": typ, "level": lvl, "head": head, "area": area, "desc": desc, "on": on, "off": off, "link": link})
    return out

def area_hit(a, day):
    s = a["area"].lower()
    return any(k in s for k in day["areas"])

def day_window(day):
    d = datetime.date.fromisoformat(day["date"])
    return (datetime.datetime.combine(d, datetime.time(5, 0), NZ), datetime.datetime.combine(d, datetime.time(23, 0), NZ))

# ---------- 2. 预报 ----------
def fetch_forecast():
    q = urllib.parse.urlencode({"latitude": ",".join(str(d["lat"]) for d in DAYS), "longitude": ",".join(str(d["lon"]) for d in DAYS),
        "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,wind_gusts_10m_max",
        "timezone": "Pacific/Auckland", "forecast_days": 16})
    res = json.loads(get("https://api.open-meteo.com/v1/forecast?" + q))
    res = res if isinstance(res, list) else [res]
    fc = {}
    for day, r in zip(DAYS, res):
        dd = r.get("daily") or {}
        if day["date"] in dd.get("time", []):
            j = dd["time"].index(day["date"])
            fc[day["date"]] = {"code": dd["weather_code"][j], "lo": dd["temperature_2m_min"][j], "hi": dd["temperature_2m_max"][j],
                               "pop": dd["precipitation_probability_max"][j], "mm": dd["precipitation_sum"][j],
                               "wind": dd["wind_speed_10m_max"][j], "gust": dd.get("wind_gusts_10m_max", [None] * 99)[j]}
    return fc

# ---------- 3. 决策 ----------
def decide(day, f, alerts, now):
    notes = []          # (level, text)
    hit_alerts = []
    w0, w1 = day_window(day)
    dd = datetime.date.fromisoformat(day["date"])
    for a in alerts:
        if not area_hit(a, day) or not a["on"] or not a["off"]: continue
        overlap = a["on"] < w1 and a["off"] > w0
        lingering = a["type"] in ("snow", "road_snow") and not overlap and 0 < (w0 - a["off"]).total_seconds() <= 20 * 3600
        if not overlap and not lingering: continue
        hit_alerts.append(a)
        span = fmt_span(a["on"], a["off"]); short = a["desc"][:140]
        if lingering:
            notes.append((1, "头天 %s 有%s（%s），早上路面可能残雪结冰。出发前看 NZTA，雪链带上。" % (a["area"], a["head"].split(" - ")[0], span)))
        elif a["type"] == "road_snow":
            notes.append((2, "%s 道路降雪警告（%s）：%s 雪链装车上，出发前看 NZTA。%s" % (a["area"], span, short, day.get("pass_alt", ""))))
        elif a["type"] == "snow":
            if a["level"] in ("orange", "red"):
                notes.append((3, "%s %s大雪警报（%s）：%s 别一早上路，等 NZTA 说通了再走。%s" % (a["area"], "红色" if a["level"] == "red" else "橙色", span, short, day.get("pass_alt", ""))))
            else:
                notes.append((1, "%s 大雪关注（%s），有可能升级成警报，出发前再看一次。" % (a["area"], span)))
        elif a["type"] == "rain":
            if day.get("milford"):
                notes.append((3 if a["level"] in ("orange", "red") else 2, "Fiordland 大雨%s（%s）：SH94 有关闭风险。早上先看 Milford Road 状态页；封了打 Cruise Milford 03 398 1250；开着就照去，雨中瀑布最壮观。" % ("警报" if a["level"] in ("orange", "red") else "关注", span)))
            elif day.get("westcoast"):
                notes.append((2 if a["level"] in ("orange", "red") else 1, "%s 大雨%s（%s）：SH6 / SH73 可能塌方封路，出发前看 NZTA。%s" % (a["area"], "警报" if a["level"] in ("orange", "red") else "关注", span, day.get("pass_alt", ""))))
            else:
                notes.append((1, "%s 大雨%s（%s）：户外缩短，%s" % (a["area"], "警报" if a["level"] in ("orange", "red") else "关注", span, day.get("sunset_alt", "日落别指望。"))))
        elif a["type"] == "wind":
            if day.get("milford"):
                notes.append((2, "Fiordland 强风%s（%s）：游船可能取消，出发前看邮件或打 03 398 1250。" % ("警报" if a["level"] in ("orange", "red") else "关注", span)))
            elif day.get("pass"):
                notes.append((1, "%s 强风%s（%s）：%s 高处横风，慢开。" % (a["area"], "警报" if a["level"] in ("orange", "red") else "关注", span, day["pass"])))
            elif day.get("hike"):
                notes.append((1, "%s 强风%s（%s）：Hooker 的吊桥风大会关，到了看牌子。" % (a["area"], "警报" if a["level"] in ("orange", "red") else "关注", span)))
            else:
                notes.append((1, "%s 强风%s（%s）。" % (a["area"], "警报" if a["level"] in ("orange", "red") else "关注", span)))
    # 预报规则
    if f:
        k, _ = kind(f["code"]); pop = f["pop"] or 0; mm = f["mm"] or 0; lo = f["lo"]; wind = f["wind"] or 0
        if day.get("pass"):
            if f["code"] in SNOW: notes.append((2, "预报有雪：雪链装车上，出发前看 NZTA。%s" % day.get("pass_alt", "")))
            elif lo is not None and lo <= 0: notes.append((1, "最低 %d°C，早上山口路面可能结冰。%s" % (round(lo), day.get("depart", "等太阳出来再翻山"))))
        if day.get("milford"):
            if mm >= 25 and not any(a["type"] == "rain" for a in hit_alerts):
                notes.append((2, "预报 %d mm 大雨：峡湾下雨是常态，瀑布最壮观，但雨大 SH94 会关。头天晚上和当天早上各看一次状态页。" % round(mm)))
            if wind >= 55 and not any(a["type"] == "wind" for a in hit_alerts):
                notes.append((1, "预报风 %d km/h：船可能晃，晕船药先吃。" % round(wind)))
        if day.get("hike") and (mm >= 5 or f["code"] in SNOW):
            notes.append((1, "%s：%s" % (day["hike"], day["hike_alt"])))
        if day.get("sunset") and (pop >= 70 or mm >= 8):
            notes.append((1, "%s 日落大概率没有：%s" % (day["sunset"], day["sunset_alt"])))
        if day.get("outdoor") and (pop >= 60): notes.append((1, day["outdoor"]))
        if day.get("arrive") and wind >= 60: notes.append((1, "落地那晚风大，可能晚点，Sudima 24 小时前台，不急。"))
    lvl = max([n[0] for n in notes], default=0)
    if not notes and f: notes.append((0, "照常。" + (day.get("note", ""))))
    elif not notes: notes.append((0, "还没进 16 天预报范围。"))
    return lvl, notes, hit_alerts

def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist", "nz", "wx.json")
    now = datetime.datetime.now(NZ)
    try: alerts = fetch_alerts()
    except Exception as e: alerts = []; print("alerts failed:", e, file=sys.stderr)
    try: fc = fetch_forecast()
    except Exception as e: fc = {}; print("forecast failed:", e, file=sys.stderr)
    days_out, used = [], {}
    for day in DAYS:
        f = fc.get(day["date"])
        lvl, notes, hits = decide(day, f, alerts, now)
        for a in hits: used.setdefault(a["link"], (a, []))[1].append(day["date"])
        dd = datetime.date.fromisoformat(day["date"])
        row = {"date": day["date"], "d": "%d/%d" % (dd.month, dd.day), "wd": "周" + ZH_WD[dd.weekday()], "place": day["place"],
               "level": lvl, "status": LEVEL[lvl], "notes": [n[1] for n in notes if n[1]]}
        if f:
            k, ico = kind(f["code"])
            row["fc"] = {"kind": k, "icon": ico, "lo": f["lo"], "hi": f["hi"], "pop": f["pop"], "mm": f["mm"], "wind": f["wind"], "code": f["code"]}
            row["sum"] = "%s %s～%s°C · 降水 %s%%" % (k, round(f["lo"]) if f["lo"] is not None else "?", round(f["hi"]) if f["hi"] is not None else "?", f["pop"] if f["pop"] is not None else "?")
        days_out.append(row)
    alerts_out = [{"head": a["head"], "level": a["level"], "type": a["type"], "area": a["area"], "span": fmt_span(a["on"], a["off"]),
                   "desc": a["desc"][:300], "days": ds, "link": a["link"]} for a, ds in used.values()]
    alerts_out.sort(key=lambda x: x["days"][0])
    res = {"generated_at": now.isoformat(), "generated_nz": now.strftime("%m/%d %H:%M"), "n_alerts_total": len(alerts),
           "alerts": alerts_out, "days": days_out,
           "src": {"metservice": "https://www.metservice.com/warnings/home", "nzta": "https://www.journeys.nzta.govt.nz/",
                   "milford": "https://www.nzta.govt.nz/projects/sh94-milford-road/sh94-milford-road-status", "cap": CAP_RSS}}
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    json.dump(res, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wx.json:", out_path, "| alerts total", len(alerts), "| on route", len(alerts_out), "|", " ".join("%s:%s" % (r["d"], r["status"]) for r in days_out))

if __name__ == "__main__":
    main()
