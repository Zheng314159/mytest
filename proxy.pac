function FindProxyForURL(url, host) {
    // 定义需要走代理的域名关键词
    var proxyDomains = [
        ".google.com",
        ".facebook.com",
        ".twitter.com",
        ".youtube.com",
        ".github.com",
        ".wikipedia.org"
    ];

    // 遍历域名匹配表
    for (var i = 0; i < proxyDomains.length; i++) {
        if (dnsDomainIs(host, proxyDomains[i]) || shExpMatch(host, "*" + proxyDomains[i])) {
            return "SOCKS5 127.0.0.1:1080";
        }
    }

    // 其他域名默认直连
    return "DIRECT";
}
