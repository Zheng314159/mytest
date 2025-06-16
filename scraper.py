"""
Playwright 爬虫示例脚本 (Python 异步版本)

使用方法:
1. 安装依赖:
   pip install playwright
   playwright install

2. 保存此脚本为 scraper.py

3. 运行示例:
   python scraper.py https://example.com "h1" --output result.csv

参数:
    url      要抓取的页面 URL
    selector CSS 选择器，用于定位要提取的元素
    --output 指定输出的 CSV 文件 (默认为 output.csv)
"""

import argparse
import asyncio
from playwright.async_api import async_playwright
import csv


async def scrape(url: str, selector: str, output: str):
    """
    使用 Playwright 异步 API 打开浏览器、访问页面，抓取匹配 selector 的文本内容并保存到 CSV。
    """
    async with async_playwright() as p:
        # 启动 Chromium 浏览器 (headless 模式)
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        # 跳转到目标 URL
        await page.goto(url)
        # 等待页面内容加载 (可根据实际情况调整或添加更多等待)
        await page.wait_for_load_state("networkidle")
        # 查询所有匹配 CSS 选择器的元素
        elements = await page.query_selector_all(selector)
        data: list[str] = []
        # 提取每个元素的文本
        for el in elements:
            text = await el.inner_text()
            data.append(text.strip())
        await browser.close()

    # 将提取的数据写入 CSV
    with open(output, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["text"])
        for d in data:
            writer.writerow([d])

    print(f"共抓取到 {len(data)} 条数据，已保存至 {output}")


def main():
    parser = argparse.ArgumentParser(description="使用 Playwright 抓取指定页面的文本数据")
    parser.add_argument("url", help="要抓取的页面 URL")
    parser.add_argument("selector", help="CSS 选择器，用于定位要提取的元素")
    parser.add_argument("--output", default="output.csv", help="输出的 CSV 文件名 (默认为 output.csv)")
    args = parser.parse_args()

    # 执行异步爬虫任务
    asyncio.run(scrape(args.url, args.selector, args.output))


if __name__ == "__main__":
    main()
