poetry completions bash >> ~/.bash_completion
echo 'eval "$(task --completion bash)"' >> ~/.bashrc
task --completion bash > /etc/bash_completion.d/task


