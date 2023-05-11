import gym

env = gym.make("LunarLander-v2",
                continuous: bool = False,
                gravity: float = -10.0,
                enable_wind: float = 15.0,
                turbulence_power: float = 1.5,)

env.action_space.seed(42)

observation, info = env.reset(seed=42)

for _ in range(1000):
    observation, reward, terminated, truncated, info = env.step(env.action_space.sample())

    if terminated or truncated:
        observation, info = env.reset()

env.close()