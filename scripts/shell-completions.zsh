poetry completions zsh > ~/.zfunc/_poetry
fpath+=~/.zfunc
autoload -Uz compinit && compinit
echo 'eval "$(task --completion zsh)"' >> ~/.zshrc
task --completion zsh  > /usr/local/share/zsh/site-functions/_task



