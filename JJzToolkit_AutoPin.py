from os import popen
from re import findall
from time import sleep

def execCmd(cmd):
	cmd_output = popen(cmd)
	content = cmd_output.read()
	cmd_output.close()
	return content

def getIP(content):
	content = content.splitlines()
	return findall(r"\d+\.?\d+\.?\d+\.?\d+", content[-1])[0]

def showLogo():
	lines = r"""       _      _ ______                 _        _____ _                ___   ___  __ 
      | |    | |___  /      /\        | |      |  __ (_)              / _ \ / _ \/_ |
      | |    | |  / /_____ /  \  _   _| |_ ___ | |__) | _ __   __   _| | | | | | || |
  _   | |_   | | / /______/ /\ \| | | | __/ _ \|  ___/ | '_ \  \ \ / / | | | | | || |
 | |__| | |__| |/ /__    / ____ \ |_| | || (_) | |   | | | | |  \ V /| |_| | |_| || |
  \____/ \____//_____|  /_/    \_\__,_|\__\___/|_|   |_|_| |_|   \_/  \___(_)___(_)_|""".splitlines()
	for line in lines:
		print(line)
		sleep(0.2)
	sleep(0.5)

def main():
	print('\n[INFO] 执行命令“ipconfig”')
	content = execCmd('ipconfig')
	print(content)

	ip = getIP(content)
	print('[INFO] 默认网关为提取为：%s' % ip)

	print("\n[INFO] 执行命令“ping %s”" % ip)
	content = execCmd("ping {}".format(ip))
	print(content)

if __name__ == '__main__':
	showLogo()
	main()
	input("[INFO] 这网关要是ping通了，你自己吃了他。满意了吧？按回车键退出......")
