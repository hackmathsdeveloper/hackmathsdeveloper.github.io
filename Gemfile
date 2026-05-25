source "https://rubygems.org"

gem "jekyll", "~> 4.2.0"
gem "jekyll-sass-converter", "~> 2.2"
gem "jekyll-seo-tag", "~> 2.8"
gem "jekyll-sitemap", "~> 1.4"
gem "jekyll-feed", "~> 0.17"
gem "jekyll-paginate", "~> 1.1"
gem "ffi", "< 1.17"

# Windows and JRuby does not include zoneinfo files
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock http_parser.rb to compatible version on newer Rubies
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
