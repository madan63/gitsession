from matplotlib import pyplot as plt
import random
import numpy as np

teams = {'DC': 'Delhi Capitals', 'CSK': 'Chennai Super Kings', 'SRH': 'Sun Risers Hyderabad', 'KKR':'Kolkata Knight Riders', 
'KXIP': 'Kings XI Punjab', 'RR': 'Rajastan Royals', 'RCB': 'Royal Challengers Bangalore', 'MI':'Mumbai Indians'}

for i, team in enumerate(teams,1):
	print(f'{i}. {team} {teams[team]}\n')
print('\n')
team1 = input('Enter first team: ')
print('\n')
team2 = input('Enter second team: ')

overs = list(range(1,21))

team1_scores = [random.choice(range(36)) for i in overs]
team1_total = sum(team1_scores)
team2_scores = [random.choice(range(36)) for i in overs]
team2_total = sum(team2_scores)
width = 0.35  # the width of the bars

x = np.arange(len(overs))

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, team1_scores, width, label=f'{team1} Total:{team1_total}')
rects2 = ax.bar(x + width/2, team2_scores, width, label=f'{team2} Total:{team2_total}')

ax.set_ylabel('scores')
ax.set_title('IPL Match-20 {team1} vs {team2}'.format(team1=team1, team2=team2))
ax.set_xticks(overs)
ax.set_xlabel('overs')
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.show()