echo "Cloning Repo...."
git clone https://github.com/ZauteKm/ZoRadioBot.git /ZoRadioBot
cd /ZoRadioBot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
