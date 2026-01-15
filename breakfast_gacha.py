#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
早餐抽卡系统 - 决定今天吃什么！
"""

import random
from dataclasses import dataclass
from typing import List


@dataclass
class BreakfastItem:
    """早餐物品类"""
    name: str
    rarity: str
    emoji: str
    description: str


class BreakfastGacha:
    """早餐抽卡系统"""

    def __init__(self):
        # 定义不同稀有度的早餐选项
        self.menu = {
            "N": [  # 普通
                BreakfastItem("豆浆油条", "N", "🥯", "经典组合，朴实无华"),
                BreakfastItem("白粥配咸菜", "N", "🥣", "清淡养胃"),
                BreakfastItem("馒头配鸡蛋", "N", "🥚", "简单满足"),
                BreakfastItem("包子", "N", "🥟", "皮薄馅大"),
                BreakfastItem("烧饼", "N", "🫓", "香脆可口"),
            ],
            "R": [  # 稀有
                BreakfastItem("小笼包", "R", "🥟", "汤汁鲜美，一口入魂"),
                BreakfastItem("牛肉面", "R", "🍜", "汤浓面劲，能量满满"),
                BreakfastItem("煎饼果子", "R", "🌯", "加两个蛋！"),
                BreakfastItem("馄饨", "R", "🥣", "皮薄馅嫩，汤鲜味美"),
                BreakfastItem("豆腐脑", "R", "🍮", "咸甜之争，你选哪边"),
            ],
            "SR": [  # 史诗
                BreakfastItem("广式早茶", "SR", "🍵", "虾饺烧卖叉烧包，精致生活"),
                BreakfastItem("日式拉面", "SR", "🍜", "豚骨汤底，浓郁醇厚"),
                BreakfastItem("韩式石锅拌饭", "SR", "🍚", "营养丰富，滋滋作响"),
                BreakfastItem("法式可颂", "SR", "🥐", "外酥内软，层次分明"),
                BreakfastItem("意式帕尼尼", "SR", "🥪", "热压三明治，芝士拉丝"),
            ],
            "SSR": [  # 传说
                BreakfastItem("海鲜自助早餐", "SSR", "🦞", "帝王蟹、三文鱼、生蚝通通拿下！"),
                BreakfastItem("米其林早餐", "SSR", "⭐", "大厨精心烹饪，尊贵体验"),
                BreakfastItem("和牛牛排早餐", "SSR", "🥩", "A5和牛，入口即化"),
                BreakfastItem("豪华酒店早午餐", "SSR", "🏨", "香槟+龙虾+无限续杯"),
                BreakfastItem("妈妈亲手做的早餐", "SSR", "❤️", "世界上最温暖的味道"),
            ]
        }

        # 稀有度概率
        self.probability = {
            "N": 50,    # 50%
            "R": 30,    # 30%
            "SR": 15,   # 15%
            "SSR": 5    # 5%
        }

        # 稀有度颜色
        self.colors = {
            "N": "\033[37m",      # 白色
            "R": "\033[34m",      # 蓝色
            "SR": "\033[35m",     # 紫色
            "SSR": "\033[33m",    # 金色
        }
        self.reset = "\033[0m"

    def roll_rarity(self) -> str:
        """抽取稀有度"""
        rand = random.randint(1, 100)
        cumulative = 0

        for rarity, prob in self.probability.items():
            cumulative += prob
            if rand <= cumulative:
                return rarity

        return "N"

    def draw(self) -> BreakfastItem:
        """抽卡"""
        rarity = self.roll_rarity()
        items = self.menu[rarity]
        return random.choice(items)

    def show_card(self, item: BreakfastItem):
        """展示抽到的卡片"""
        color = self.colors[item.rarity]

        print("\n" + "═" * 50)
        print(f"{color}★☆★ 抽卡结果 ★☆★{self.reset}")
        print("═" * 50)
        print(f"\n{color}【{item.rarity}】{item.emoji} {item.name}{self.reset}")
        print(f"    {item.description}")
        print("\n" + "═" * 50)

        # 根据稀有度显示不同评语
        if item.rarity == "N":
            print("💭 朴实的一天，从简单的早餐开始~")
        elif item.rarity == "R":
            print("💭 不错的选择！今天会有好心情~")
        elif item.rarity == "SR":
            print("💭 运气不错！今天要吃顿好的！")
        elif item.rarity == "SSR":
            print("💭 天啊！欧皇附体！今天太幸运了！")
        print("═" * 50 + "\n")

    def ten_pull(self):
        """十连抽"""
        print("\n" + "◆" * 50)
        print("🎰 十连抽开始！")
        print("◆" * 50 + "\n")

        results = []
        for i in range(10):
            item = self.draw()
            results.append(item)
            color = self.colors[item.rarity]
            print(f"{i+1}. {color}[{item.rarity}]{self.reset} {item.emoji} {item.name}")

        print("\n" + "◆" * 50)

        # 推荐最稀有的一餐
        rarity_order = {"SSR": 4, "SR": 3, "R": 2, "N": 1}
        best = max(results, key=lambda x: rarity_order[x.rarity])

        color = self.colors[best.rarity]
        print(f"\n🎯 推荐今天吃：{color}{best.emoji} {best.name}{self.reset}")
        print(f"   {best.description}")
        print("◆" * 50 + "\n")

    def menu_list(self):
        """显示菜单"""
        print("\n" + "━" * 50)
        print("📋 早餐抽卡菜单")
        print("━" * 50)

        for rarity, items in self.menu.items():
            color = self.colors[rarity]
            print(f"\n{color}【{rarity}级稀有度】{self.reset}")
            for item in items:
                print(f"  • {item.emoji} {item.name}")

        print("\n" + "━" * 50 + "\n")


def main():
    """主函数"""
    print("\n╔════════════════════════════════════════╗")
    print("║       🌟 早餐抽卡系统 🌟               ║")
    print("║     今天早餐吃什么？让命运决定！        ║")
    print("╚════════════════════════════════════════╝")

    gacha = BreakfastGacha()

    while True:
        print("\n请选择操作：")
        print("1. 单抽")
        print("2. 十连抽")
        print("3. 查看菜单")
        print("4. 退出")

        choice = input("\n请输入选项 (1-4): ").strip()

        if choice == "1":
            item = gacha.draw()
            gacha.show_card(item)
        elif choice == "2":
            gacha.ten_pull()
        elif choice == "3":
            gacha.menu_list()
        elif choice == "4":
            print("\n祝你今天用餐愉快！再见~ 👋\n")
            break
        else:
            print("❌ 无效的选项，请重新选择！")


def demo():
    """自动演示模式"""
    print("\n╔════════════════════════════════════════╗")
    print("║       🌟 早餐抽卡系统 🌟               ║")
    print("║     今天早餐吃什么？让命运决定！        ║")
    print("╚════════════════════════════════════════╝")

    gacha = BreakfastGacha()

    print("\n📋 自动演示模式 - 为你抽卡！\n")

    # 单抽演示
    print("【单抽演示】")
    print("─" * 50)
    item = gacha.draw()
    gacha.show_card(item)

    # 十连抽演示
    print("\n【十连抽演示】")
    gacha.ten_pull()


if __name__ == "__main__":
    import sys

    # 如果有命令行参数 --demo，运行演示模式
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        demo()
    else:
        main()
