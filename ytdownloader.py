import sys

from pytube import YouTube
from pytube.exceptions import RegexMatchError
from rich.panel import Panel
from rich import print


print(Panel.fit("[green]Введи ссылку на видео[/green]"))
url = input()
try:
	yt = YouTube(url)
except RegexMatchError:
	print(Panel.fit("[red]Произошла ошибка. Проверь ссылку[/red]"))
	sys.exit()

try:
	print(Panel.fit("[green]Доступные разрешения видео:[/green]"))
	for stream in yt.streams.filter(progressive=True):
		print(stream.resolution)
except RegexMatchError:
	print(Panel.fit("[red]Произошла ошибка. Проверь ссылку[/red]"))


print(Panel.fit("[green]Введи разрешение в точности как и написано выше или же введи 0 чтобы скачать видео в лучшем разрешении[/green]"))
resolution = input()


if resolution == "0":
	yt.streams.filter(progressive=True).last().download()
	print(Panel.fit(f"[green]Видео успешно загружено в {yt.streams.filter(progressive=True).last()['res']}[/green]"))
else:
	try:
		yt.streams.filter(res=resolution).first().download()
		print(Panel.fit(f"[green]Видео успешно загружено в {resolution}[/green]"))
	except:
		print(Panel.fit("[red]Произошла ошибка. Проверь правильно ли введено разрешение[/red]"))
