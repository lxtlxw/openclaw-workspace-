/**
 * RTX 5070 Ti 京东价格爬虫
 */

const https = require('https');

const BRANDS = [
    "七彩虹 5070 Ti",
    "华硕 5070 Ti",
    "微星 5070 Ti",
    "技嘉 5070 Ti",
    "影驰 5070 Ti",
    "索泰 5070 Ti"
];

function search(keyword) {
    return new Promise((resolve) => {
        const url = `https://search.jd.com/Search?keyword=${encodeURIComponent(keyword)}&enc=utf-8`;
        
        https.get(url, {
            headers: {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
        }, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => {
                console.log(`✓ ${keyword}: ${data.length} bytes`);
                resolve(data.length > 0);
            });
        }).on('error', (e) => {
            console.log(`✗ ${keyword}: ${e.message}`);
            resolve(false);
        });
    });
}

async function main() {
    console.log("=" .repeat(60));
    console.log("RTX 5070 Ti 京东价格爬虫");
    console.log("=" .repeat(60));
    
    for (const brand of BRANDS) {
        await search(brand);
    }
    
    console.log("\n提示：京东有反爬，完整数据需要 Selenium 或 API");
}

main();
