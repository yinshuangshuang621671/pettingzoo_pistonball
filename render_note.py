import pettingzoo
from pettingzoo.classic import tictactoe_v3
import torch

# pettingzoo.__version__

from pettingzoo.butterfly import pistonball_v6

parallel_env = pistonball_v6.parallel_env(render_mode="human", max_cycles=159)
observations = parallel_env.reset(seed=42)
i = 0
while parallel_env.agents:
    # this is where you would insert your policy
    actions = {agent: parallel_env.action_space(agent).sample() for agent in parallel_env.agents}
    print('actions', actions)
    observations, rewards, terminations, truncations, infos = parallel_env.step(actions)
    print('rewards', rewards, 'end')
    i = i + 1
    print(observations['piston_19'].shape)
parallel_env.close()
print(i)

# 原文链接：https: // blog.csdn.net / CAIYUNFREEDOM / article / details / 131208329