import os

import tensorflow as tf

from tensorforce.agents import Agent
from tensorforce.environments import Environment
from tensorforce.execution import Runner


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.logging.set_verbosity(v=tf.logging.ERROR)


# Create an OpenAI-Gym environment
environment = Environment.create(environment='gym', level='CartPole-v1')

# Create a PPO agent
agent = Agent.create(
    agent='ppo', environment=environment,
    # Automatically configured network
    network='auto',
    # Optimization
    batch_size=10, update_frequency=2, learning_rate=1e-3, subsampling_fraction=0.2,
    optimization_steps=5,
    # Reward estimation
    likelihood_ratio_clipping=0.2, discount=0.99, estimate_terminal=False,
    # Critic
    critic_network='auto',
    critic_optimizer=dict(optimizer='adam', multi_step=10, learning_rate=1e-3),
    # Preprocessing
    preprocessing=None,
    # Exploration
    exploration=0.0, variable_noise=0.0,
    # Regularization
    l2_regularization=0.0, entropy_regularization=0.0,
    # TensorFlow etc
    name='agent', device=None, parallel_interactions=1, seed=None, execution=None, saver=None,
    summarizer=None, recorder=None
)

# Initialize the runner
runner = Runner(agent=agent, environment=environment)

# Start the runner
runner.run(num_episodes=300)
runner.close()
