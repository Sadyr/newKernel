UPDATE fqH_options SET option_value = replace(option_value, 'https://lih.yls.mybluehost.me', 'https://almatyfinance.kz') WHERE option_name = 'home' OR option_name = 'siteurl';
UPDATE fqH_posts SET post_content = REPLACE (post_content, 'https://lih.yls.mybluehost.me', 'https://almatyfinance.kz');
UPDATE fqH_comments SET comment_content = REPLACE (comment_content, 'https://lih.yls.mybluehost.me', 'https://almatyfinance.kz');
UPDATE fqH_comments SET comment_author_url = REPLACE (comment_author_url, 'https://lih.yls.mybluehost.me', 'https://almatyfinance.kz');