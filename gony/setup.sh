mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"kws120790@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
enableXsrfProtection=false\n\
port = $PORT\n\
\n
" > ~/.streamlit/config.toml