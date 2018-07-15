# Sitemap Health Checker

Xml health check with status codes and elapsed times.

# Usage

 * Generating config file.

    `python health-checker.py --generate`
    * Example config
 
        `{
            "debug": false,
            "delay": 1,
            "headers": {
                "User-Agent": "sitemap-health-checker"
            },
                "output": "json",
                "url": "http://www.mysite.com/sitemap.xml"
        }`
    
        Debug(false) : Outputs url, status_code and elapsed time to console when parameter True.

        Delay(1): Delay between requests.

        User-Agent: Setting custom user-agent to request header.

        Output(json, csv): log file output type.

        Url: Target site xml url.

 * Executing with config file.

    `python health-checker.py --config .\config.json`

* Builth With

    * bs4 (BeatifulSoup) 
    * requests