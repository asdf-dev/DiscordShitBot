#base img
FROM python:latest

#workdir
WORKDIR /monster

#copy bot to docker
COPY bot.py .

#install discord shit
RUN python3 -m pip install -U discord.py

#run bot
CMD ["python3", "bot.py"]