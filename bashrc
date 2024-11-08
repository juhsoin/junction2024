export PATH=:/root/scripts/:$PATH
export XDG_CONFIG_HOME=:/root/

vim () {
	XDG_CONFIG_HOME=/root/ /root/bin/nvim $1
}
