mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"kws1207@kaist.ac.kr\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml