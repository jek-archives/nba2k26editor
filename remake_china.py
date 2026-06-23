import re
import os

# ----------------- TRANSLATION DICTIONARY -----------------
TR_MAP = {
    # Teams
    "76人": "76ers",
    "雄鹿": "Bucks",
    "公牛": "Bulls",
    "骑士": "Cavaliers",
    "凯尔特人": "Celtics",
    "快船": "Clippers",
    "灰熊": "Grizzlies",
    "老鹰": "Hawks",
    "热火": "Heat",
    "黄蜂": "Hornets",
    "爵士": "Jazz",
    "国王": "Kings",
    "尼克斯": "Knicks",
    "湖人": "Lakers",
    "魔术": "Magic",
    "独行侠": "Mavericks",
    "小牛": "Mavericks Retro",
    "篮网": "Nets",
    "掘金": "Nuggets",
    "步行者": "Pacers",
    "鹈鹕": "Pelicans",
    "活塞": "Pistons",
    "猛龙": "Raptors",
    "火箭": "Rockets",
    "马刺": "Spurs",
    "太阳": "Suns",
    "雷霆": "Thunder",
    "森林狼": "Timberwolves",
    "开拓者": "Trail Blazers",
    "勇士": "Warriors",
    "奇才": "Wizards",
    "超音速": "Supersonics",
    "世界/全明星": "World/All-Star",

    # Players
    "特雷杨": "Trae Young",
    "塔图姆": "Jayson Tatum",
    "乔丹": "Michael Jordan",
    "皮蓬": "Scottie Pippen",
    "沃克": "Kemba Walker",
    "保罗": "Chris Paul",
    "利拉德": "Damian Lillard",
    "东七七": "Luka Doncic",
    "克拉克森": "Jordan Clarkson",
    "科比": "Kobe Bryant",
    "布克": "Devin Booker",
    "哈达威": "Penny Hardaway",
    "麦迪": "Tracy McGrady",
    "华子": "Anthony Edwards",
    "欧文": "Kyrie Irving",
    "艾弗森": "Allen Iverson",
    "戴维斯": "Anthony Davis",
    "杜兰特": "Kevin Durant",
    "唐斯": "Karl-Anthony Towns",
    "威斯布鲁克": "Russell Westbrook",
    "诺维斯基": "Dirk Nowitzki",
    "斯托克顿": "John Stockton",
    "霍乐迪": "Jrue Holiday",
    "巴特勒": "Jimmy Butler",
    "莫兰特": "Ja Morant",
    "普尔": "Jordan Poole",
    "坎宁安": "Cade Cunningham",
    "沃尔": "John Wall",
    "詹姆斯": "LeBron James",
    "科沃尔": "Kyle Korver",
    "安东尼": "Carmelo Anthony",
    "拉文": "Zach LaVine",
    "库里": "Stephen Curry",
    "汤普森": "Klay Thompson",
    "格林": "Draymond Green",
    "约基奇": "Nikola Jokic",
    "恩比德": "Joel Embiid",
    "字母哥": "Giannis Antetokounmpo",
    "威少": "Russell Westbrook",

    # Gear Categories & Brands
    "特殊物品": "Special Items",
    "帽子": "Hats",
    "发带": "Headbands",
    "耳机": "Headphones",
    "眼镜": "Glasses",
    "球鞋阿迪": "Adidas Sneakers",
    "球鞋AIR-乔丹": "Air Jordan Sneakers",
    "Nike AIR系列": "Nike Air Series",
    "JORDAN系列": "Jordan Series",
    "Adidas系列": "Adidas Series",
    "Nike系列": "Nike Series",
    "Under Armour系列": "Under Armour Series",
    "科比四-科比11系列": "Kobe 4 - Kobe 11 Series",
    "科比AD系列": "Kobe AD Series",
    "球鞋PG KD": "PG & KD Series",
    "球鞋詹姆斯16": "LeBron 16 Series",
    "球鞋AIR-乔丹31": "Air Jordan 31 Series",
    "阿迪": "Adidas",
    "耐克": "Nike",

    # Colors
    "深灰": "Dark Grey",
    "浅灰": "Light Grey",
    "黑白": "Black & White",
    "红白": "Red & White",
    "白蓝": "White & Blue",
    "粉蓝": "Pink & Blue",
    "粉色": "Pink",
    "紫色": "Purple",
    "黄色": "Yellow",
    "黑色": "Black",
    "白色": "White",
    "红色": "Red",
    "蓝色": "Blue",
    "青色": "Teal",
    "灰色": "Grey",
    "绿色": "Green",
    "金色": "Gold",
    "银色": "Silver",
    "橙色": "Orange",
    "棕色": "Brown",
    "粉": "Pink",
    "紫": "Purple",
    "黄": "Yellow",
    "黑": "Black",
    "白": "White",
    "红": "Red",
    "蓝": "Blue",
    "青": "Teal",
    "灰": "Grey",
    "绿": "Green",
    "金": "Gold",
    "银": "Silver",
    "橙": "Orange",
    "棕": "Brown",
    "深": "Dark ",
    "浅": "Light ",
    "炫幻": "Fantasy",

    # Gear items
    "全裹羽绒服": "Down Jacket ",
    "戴帽卫衣": "Hoodie ",
    "连帽卫衣": "Hoodie ",
    "卫衣": "Sweatshirt ",
    "紧身衣": "Compression Shirt ",
    "长袖": "Long Sleeve",
    "短袖": "Short Sleeve",
    "无袖": "Sleeveless",
    "裤子": "Pants",
    "拖鞋": "Slides",
    "短裤": "Shorts",
    "打底裤": "Tights",
    "长袜": "Long Socks",
    "短袜": "Short Socks",
    "中袜": "Mid Socks",
    "火鸡": "Turkey",
    "圣诞": "Christmas",
    "万万岁": "Anniversary",
    "赛季": "Season",
    "黄金": "Gold",
    "白银": "Silver",
    "青铜": "Bronze",
    "钻石": "Diamond",
    "水手袜": "Crew Socks",
    "个性": "Personality",
    "主要主宰": "Primary Takeover",
    "次要主宰": "Secondary Takeover",

    # Dropdowns & Options
    "球馆资料": "Arena Info",
    "资料选项": "Player Profile",
    "自建捏脸": "Custom Face Shape",
    "娱乐设置": "Cheats & Settings",
    "鞋选项": "Sneaker Settings",
    "地板": "Floor Textures",
    "用户": "User Config",
    "电脑": "CPU Config",
    "球馆": "Arena",
    "球衣": "Jersey",
    "球鞋": "Sneaker",
    "捏脸": "Face",
    "配件": "Gear",
    "动作": "Animation",
    "娱乐": "Cheats",
    "其它": "Other",
    "选择": "Select",
    "装备": "Equip",
    "卸下": "Remove",
    "取消": "Remove / Cancel",
    "使用": "Apply",
    "锁定": "Lock",
    "版本": "Version",
    "切换": "Switch",
    "初始化": "Initialize",
    "所有": "All",
    "删除": "Delete",
    "清除": "Clear",
    "比赛": "Game",
    "无限": "Infinite",
    "点数": "Points/VC",
    "真实": "Always",
    "必中": "Green / Perfect",
    "流汗": "Sweat",
    "画质": "Graphics / Detail",
    "镜头": "Camera",
    "缩放": "Zoom",
    "超": "Super",
    "广角": "Wide Angle",
    "转身": "Spin",
    "背后": "Behind Back",
    "跳投": "Jump Shot",
    "摆脱": "Escape",
    "出手": "Release",
    "扣篮": "Dunk",
    "包": "Package",
    "庆祝": "Celebration",
    "指示": "Indicator",
    "完美": "Perfect",
    "特效": "FX",
    "球": "Ball",
    "花": "FX",
    "类型": "Type",
    "名字": "Name",
    "选择": "Select",
    "自定义": "Custom",
    "包厢": "Suite",
    "视角": "View",
    "大学": "College",
    "来自": "From",
    "地": "Hometown",
    "首发": "Starter",
    "徽章": "Badges",
    "满": "Max",
    "鞋": "Sneakers",
    "左": "Left",
    "右": "Right",
    "双": "Both",
    "袜": "Socks",
    "水手": "Crew",
    "打底": "Tights",
    "长": "Long",
    "短": "Short",
    "腕": "Wrist",
    "指": "Finger",
    "膝": "Knee",
    "腿": "Leg",
    "肘": "Elbow",
    "髌骨": "Patella",
    "带": "Band",
    "填充": "Padded",
    "衣袖": "Sleeve",
    "双臂": "Both Arms",
    "护": "Sleeve/Pad",
    "肩": "Shoulder",
    "橡胶": "Rubber",
    "环": "Ring",
    "腕带": "Wristband",
    "铅笔": "Pinstripe",
    "条": "Pinstripe",
    "迷你": "Mini",
    "斑": "Spots",
    "点": "Spots",
    "骨": "Bone",
    "上": "Upper",
    "下": "Lower",
    "翼": "Wing",
    "孔": "Hole",
    "眉": "Brow",
    "眼": "Eye",
    "耳": "Ear",
    "垂": "Lobe",
    "唇": "Lip",
    "巴": "Chin",
    "酒窝": "Dimple",
    "颊": "Cheek",
    "太阳": "Temple",
    "穴": "Temple",
    "形": "Style",
    "头": "Hair",
    "发": "Hair",
    "胡": "Beard",
    "须": "Beard",
    "预": "Pre",
    "设": "Set",
    "毛": "Hair",
    "由": "By",
    "输入": "Input",
    "顺位": "Order/Pick",
    "验证": "Verify",
    "登录": "Login",
    "解锁": "Unlock",
    "作者": "Author",
    "交流群": "Group",
    "隐藏": "Hidden",
    "次要": "Secondary",
    "主宰": "Takeover",
    "状态": "Status",
    "图标": "Icon",
    "自建": "Custom",
    "打板": "Backboard",
    "电影": "Movie",
    "极慢": "Very Slow",
    "较慢": "Slow",
    "较快": "Fast",
    "极快": "Very Fast",
    "主客": "Home/Away",
    "球衣列表": "Jersey List",
    "大学": "College",
    "顺位": "Pick",
    "年龄": "Age",
    "徽章": "Badges",
    "满": "Max",
    "鞋": "Sneakers",
    "双膝": "Both Knees",
    "双髌": "Both Patellas",
    "短打底": "Short Tights",
    "长打底": "Long Tights",
    "卸下": "Remove",
    "取消": "Remove",
    "自定义": "Custom",
    "包厢": "Suite",
    "视角": "View",
    "投篮": "Shot",
    "运球": "Dribble",
    "背后": "Behind Back",
    "跳步": "Stepback",
    "扣篮": "Dunk",
    "指示": "Indicator",
    "完美": "Perfect",
    "特效": "FX",
    "球": "Ball",
    "名字": "First Name",
    "姓氏": "Last Name",
    "选择": "Select",
    "使用": "Apply",
    "锁定": "Lock",
    "版本": "Version",
    "切换": "Switch",
    "初始化": "Initialize",
    "所有": "All",
    "删除": "Delete",
    "清除": "Clear",
    "比赛": "Game",
    "无限": "Infinite",
    "点数": "VC/Points",
    "真实": "Always",
    "必中": "Perfect/Green",
    "流汗": "Sweat",
    "画质": "Graphics",
    "镜头": "Camera",
    "缩放": "Zoom",
    "超": "Super",
    "广角": "Wide Angle",
    "转身": "Spin",
    "背后": "Behind Back",
    "跳投": "Jump Shot",
    "摆脱": "Escape",
    "出手": "Release",
    "扣篮": "Dunk",
    "包": "Package",
    "庆祝": "Celebration",
    "指示": "Indicator",
    "完美": "Perfect",
    "特效": "FX",
    "球": "Ball",
    "花": "FX",
    "类型": "Type",
    "名字": "Name",
    "选择": "Select",
    "主场": "Home",
    "客场": "Away",
    "城市": "City",
    "全明星": "All-Star",
    "复古": "Retro",
    "球衣": "Jersey",
    "自定义": "Custom",
    "包厢": "Suite",
    "视角": "View",
    "大学": "College",
    "来自": "From",
    "地": "Hometown",
    "首发": "Starter",
    "徽章": "Badges",
    "满": "Max",
    "鞋": "Sneakers",
    "左": "Left",
    "右": "Right",
    "双": "Both",
    "袜": "Socks",
    "水手": "Crew",
    "打底": "Tights",
    "长": "Long",
    "短": "Short",
    "卸下护腕": "Remove Wristband",
    "卸下护指": "Remove Finger Sleeve",
    "卸下护膝": "Remove Knee Pad",
    "卸下护踝": "Remove Ankle Support",
    "卸下护肘": "Remove Elbow Sleeve",
    "卸下护腿": "Remove Leg Sleeve",
    "卸下打底裤": "Remove Tights",
    "卸下头饰": "Remove Hat",
    "卸下眼镜": "Remove Glasses",
    "卸下发带": "Remove Headband",
    "卸下耳机": "Remove Headphones",
    "卸下当前配件物品": "Remove Current Gear",
    "卸下所有配件": "Remove All Accessories",
    "卡密": "Access Code",
    "请输入卡密": "Please enter access code",
    "卡密不能为空": "Access code cannot be empty",
    "验证失败": "Wrong code! Hint: 2k26",
    "验证成功": "Access granted!",
    "提示": "Unlock Panel",
    "请输入卡密验证": "Please enter access code to verify",
    "请不要在这里输入卡密请输入教程的工作": "Index Please do not enter the card password here please enter the work of the tutorial",
    "请不要在此处输入卡密": "Please do not enter card password here",
    "请在此输入教程工作": "Please enter the work of the tutorial",
    "验证": "VERIFY",
    "验证码": "Verification Code",
    "卡密": "Card Password"
}

def translate_text(text):
    if not text:
        return text
    # Sort keys by length descending to match larger phrases first
    sorted_keys = sorted(TR_MAP.keys(), key=len, reverse=True)
    for key in sorted_keys:
        text = text.replace(key, TR_MAP[key])
    return text

def translate_array_string(s):
    # Keep team name value attributes untouched, only change display label
    # In el-option :label="item.name" :value="item.name", we replace with :label="translate(item.name)" :value="item.name"
    s = s.replace(':label="item.name"', ':label="translate(item.name)"')
    s = s.replace('{{ item.name }}', '{{ translate(item.name) }}')
    s = s.replace('{{ item.slot }}: {{ item.name }}', '{{ item.slot }}: {{ translate(item.name) }}')
    
    # Translate attributes
    s = re.sub(r'label="([^"]*)"', lambda m: f'label="{translate_text(m.group(1))}"', s)
    s = re.sub(r'placeholder="([^"]*)"', lambda m: f'placeholder="{translate_text(m.group(1))}"', s)
    s = re.sub(r'title="([^"]*)"', lambda m: f'title="{translate_text(m.group(1))}"', s)
    
    # Split by tags and translate inner text
    parts = re.split(r'(<[^>]+>)', s)
    new_parts = []
    for p in parts:
        if p.startswith('<') and p.endswith('>'):
            p = re.sub(r'label="([^"]*)"', lambda m: f'label="{translate_text(m.group(1))}"', p)
            p = re.sub(r'placeholder="([^"]*)"', lambda m: f'placeholder="{translate_text(m.group(1))}"', p)
            p = re.sub(r'title="([^"]*)"', lambda m: f'title="{translate_text(m.group(1))}"', p)
            new_parts.append(p)
        else:
            new_parts.append(translate_text(p))
            
    return "".join(new_parts)

# ----------------- LOAD ORIGINAL CHINESE HTML -----------------
with open("/Users/adajek/.gemini/antigravity-ide/brain/266604ae-b143-4680-a67d-fa24980d6a7e/.system_generated/steps/445/content.md", "r", encoding="utf-8") as f:
    html = f.read()

# Strip any Markdown header lines
html = html.split("---", 1)[-1].strip()

# ----------------- DECODE AND TRANSLATE TEMPLATE STRINGS ARRAY _0xc5c228 -----------------
match = re.search(r"var\s+(_0xc5c228)\s*=\s*\[(.*?)\];", html, re.DOTALL)
if match:
    array_content = match.group(2)
    raw_strings = re.findall(r"'(.*?)'", array_content)
    
    decoded_strings = []
    for s in raw_strings:
        try:
            escaped = s.encode('utf-8').decode('unicode_escape')
            b = bytes([ord(c) for c in escaped])
            decoded = b.decode('utf-8')
            translated = translate_array_string(decoded)
            decoded_strings.append(translated)
        except Exception:
            translated = translate_array_string(s)
            decoded_strings.append(translated)
            
    print(f"Decoded and translated {len(decoded_strings)} UI strings.")
    
    # Format the translated string array back to JS
    formatted_array = "var _0xc5c228 = [\n"
    for s in decoded_strings:
        escaped_s = s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\r', '\\r')
        formatted_array += f'  "{escaped_s}",\n'
    formatted_array += "];"
    
    html = html[:match.start()] + formatted_array + html[match.end():]
else:
    print("Error: Could not find array _0xc5c228")
    exit(1)

# ----------------- INJECT RUNTIME TRANSLATION MAP AND METHODS -----------------
# We will inject the TR_MAP and translate function inside the <head> block, and run translation hooks on loaded data files.
# Also inject Chrome compatibility helper stubs for H5GG APIs to prevent crash in normal browsers.
translation_script = """
<script>
// Runtime Translation Helper
var translationMap = """ + str(TR_MAP) + """;
function translate(text) {
    if (!text) return text;
    return translationMap[text] || text;
}

// Mock H5GG APIs for compatibility with Chrome / Safari / Normal Browsers
if (typeof setButtonImage === 'undefined') { window.setButtonImage = function() {}; }
if (typeof setWindowDrag === 'undefined') { window.setWindowDrag = function() {}; }
if (typeof setWindowRect === 'undefined') { window.setWindowRect = function() {}; }
if (typeof setWindowTouch === 'undefined') { window.setWindowTouch = function() {}; }
if (typeof setButtonAction === 'undefined') { window.setButtonAction = function() {}; }
if (typeof h5gg === 'undefined') {
    window.h5gg = {
        getRangesList: function() { return 0; },
        getRanges: function() { return []; },
        searchNumber: function() {},
        searchNearby: function() {},
        getValue: function() { return 0; },
        setValue: function() {},
        clear: function() {}
    };
}
</script>
"""

html = html.replace("<title>2K26</title>", f"<title>2K26 Editor</title>\n{translation_script}")

# ----------------- READ ORIGINAL CHINESE SCRIPT LIBRARIES FROM DOWNLOADS -----------------
with open("/Users/adajek/Downloads/jquery.min.js", "r", encoding="utf-8") as f:
    jq_code = f.read()
with open("/Users/adajek/Downloads/itemConfig.js", "r", encoding="utf-8") as f:
    ic_code = f.read()
with open("/Users/adajek/Downloads/data.js", "r", encoding="utf-8") as f:
    data_code = f.read()
with open("/Users/adajek/Downloads/teams (1).js", "r", encoding="utf-8") as f:
    teams_code = f.read()
with open("/Users/adajek/Downloads/qiuxie.js", "r", encoding="utf-8") as f:
    qx_code = f.read()

# ----------------- TRANSLATE LABELS IN MEMORY ON-THE-FLY AFTER INLINING -----------------
# This keeps internal keys/lookups in Chinese but presents translated text/labels to Vue
post_ic_script = """
for (var category in itemConfig.items) {
    itemConfig.items[category].forEach(function(item) {
        if (item.text) item.text = translate(item.text);
    });
}
"""

post_data_script = """
for (var category in data.itemList) {
    data.itemList[category].forEach(function(item) {
        if (item.text) item.text = translate(item.text);
    });
}
"""

post_qx_script = """
for (var category in qiuxie) {
    qiuxie[category].forEach(function(item) {
        if (item.label) item.label = translate(item.label);
    });
}
"""

# ----------------- REPLACE SCRIPT TAGS WITH INLINED SCRIPT CONTENT + HOOKS -----------------
html = html.replace(
    '<script src="https://ziyuan.eyashaa.cn/d/doubao/2/itemConfig.js?sign=bHesJ87ZM7hGqks7pko-K45zER8TzvjP9fH-69tR7KQ=:0"></script>',
    f'<script>\n{ic_code}\n{post_ic_script}\n</script>'
)
html = html.replace(
    '<script src="https://ziyuan.eyashaa.cn/d/doubao/2/data.js?sign=YobBqqRAmDtMp9eXY2Ts5PtilvCVJXOzGEcfCJUTIEc=:0"></script>',
    f'<script>\n{data_code}\n{post_data_script}\n</script>'
)
html = html.replace(
    '<script src="https://ziyuan.eyashaa.cn/d/doubao/2/teams.js?sign=Uu4tsMZ6BHrd-r2jntzAbG7-qjKbWyzq-IVBGVowawU=:0"></script>',
    f'<script>\n{teams_code}\n</script>'
)
html = html.replace(
    '<script src="https://ziyuan.eyashaa.cn/d/doubao/2/qiuxie.js?sign=a-ytI2Kc27W0hIk3D3BrPa0xk4zmZ9dxH3oBIjvx1Os=:0"></script>',
    f'<script>\n{qx_code}\n{post_qx_script}\n</script>'
)
html = html.replace(
    '<script src="https://ziyuan.eyashaa.cn/d/doubao/2/jquery.min.js?sign=3pZ8uv4V1QCHzXPiSkjVREbSbcrOl27_UFwd0Er0F4I=:0"></script>',
    f'<script>\n{jq_code}\n</script>'
)

# ----------------- SAVE TO INDEX.HTML -----------------
with open("/Users/adajek/.gemini/antigravity-ide/scratch/nba2k26-editor/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Combined standalone index.html written.")
