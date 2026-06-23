// Translation Dictionary for NBA 2K26 Editor
const Translation = {
  teams: {
    '76人': '76ers',
    '雄鹿': 'Bucks',
    '公牛': 'Bulls',
    '骑士': 'Cavaliers',
    '凯尔特人': 'Celtics',
    '快船': 'Clippers',
    '灰熊': 'Grizzlies',
    '老鹰': 'Hawks',
    '热火': 'Heat',
    '黄蜂': 'Hornets',
    '爵士': 'Jazz',
    '国王': 'Kings',
    '尼克斯': 'Knicks',
    '湖人': 'Lakers',
    '魔术': 'Magic',
    '独行侠': 'Mavericks',
    '小牛': 'Mavericks', // Alternate retro naming
    '篮网': 'Nets',
    '掘金': 'Nuggets',
    '步行者': 'Pacers',
    '鹈鹕': 'Pelicans',
    '活塞': 'Pistons',
    '猛龙': 'Raptors',
    '火箭': 'Rockets',
    '马刺': 'Spurs',
    '太阳': 'Suns',
    '雷霆': 'Thunder',
    '森林狼': 'Timberwolves',
    '开拓者': 'Trail Blazers',
    '勇士': 'Warriors',
    '奇才': 'Wizards',
    '超音速': 'Supersonics'
  },
  categories: {
    '特殊物品': 'Special Items',
    '帽子': 'Hats',
    '发带': 'Headbands',
    '耳机': 'Headphones',
    '眼镜': 'Glasses',
    'DIY': 'Custom DIY',
    '球鞋阿迪': 'Adidas Sneakers',
    '球鞋AIR-乔丹': 'Air Jordan Sneakers',
    'Nike AIR系列': 'Nike Air Series',
    'JORDAN系列': 'Jordan Series',
    'Adidas系列': 'Adidas Series',
    'Nike系列': 'Nike Series',
    'Under Armour系列': 'Under Armour Series',
    '科比四-科比11系列': 'Kobe 4 - Kobe 11 Series',
    '科比AD系列': 'Kobe AD Series',
    '球鞋PG KD': 'PG & KD Series',
    '球鞋詹姆斯16': 'LeBron 16 Series',
    '球鞋AIR-乔丹31': 'Air Jordan 31 Series'
  },
  labels: {
    '无': 'None',
    '默认': 'Default',
    '比赛': 'In-Game',
    '全明星': 'All-Star',
    '复古': 'Retro',
    '主场': 'Home',
    '客场': 'Away',
    '城市': 'City',
    '第一代': 'Gen 1',
    '二代': 'Gen 2',
    '三代': 'Gen 3',
    '黑': 'Black',
    '白': 'White',
    '红': 'Red',
    '黄': 'Yellow',
    '蓝': 'Blue',
    '绿': 'Green',
    '紫': 'Purple',
    '粉': 'Pink',
    '灰': 'Grey',
    '金': 'Gold',
    '银': 'Silver',
    '橙': 'Orange',
    '棕': 'Brown',
    '卸下护腕': 'Remove Wristband',
    '左髌骨带': 'Left Patella Band',
    '左填充长护膝': 'Left Padded Knee Sleeve',
    '麦迪专属护腿': 'T-Mac Leg Sleeve',
    '耐克左臂衣袖颜色': 'Nike Left Arm Sleeve Color',
    '耐克关节双臂衣袖颜色': 'Nike Both Arms Sleeve Color',
    '护膝球队颜色1': 'Knee Pads Team Color 1',
    '耐克右臂球队颜色2': 'Nike Right Arm Team Color 2',
    '取消打底裤': 'Remove Tights',
    '卸下当前配件物品': 'Remove Current Gear',
    '选择装备': 'Select Gear'
  },

  // Helper function to translate team name
  translateTeam(cnName) {
    return this.teams[cnName] || cnName;
  },

  // Helper function to translate category name
  translateCategory(cnCategory) {
    return this.categories[cnCategory] || cnCategory;
  },

  // Helper function to translate text strings (best effort)
  translateText(text) {
    if (!text) return '';
    let translated = text;
    // Replace known dictionary words
    Object.keys(this.labels).forEach(cn => {
      const reg = new RegExp(cn, 'g');
      translated = translated.replace(reg, this.labels[cn]);
    });
    return translated;
  }
};

if (typeof window !== 'undefined') {
  window.Translation = Translation;
}
