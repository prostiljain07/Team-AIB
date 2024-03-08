# ******************************************************************************************************************
# Welcome to the world of steel plate defect prediction! In this fascinating journey, we delve into the realm of 
# fault diagnosis, where we aim to categorize deviations in steel plates into seven distinct types. 
# Our mission is clear: to harness the power of various machine learning algorithms to identify and classify 
# these defects accurately.

# Fault diagnosis is akin to unraveling a mystery within a system, where deviations from the norm signal 
# potential issues. Traditionally, this process relied on the expertise of human operators armed with electronic 
# meters, maintenance manuals, and a wealth of experience. However, with the advent of machine learning, we now 
# have the opportunity to enhance this process exponentially.

# Our primary objective is twofold: to pinpoint the locations and timing of potential faults with precision, 
# utilizing the wealth of available data and our understanding of system performance. Through the seamless 
# integration of advanced algorithms and domain expertise, we strive to create a fault diagnosis system that 
# not only identifies deviations but also offers insights into their causes.

# ******************************************************************************************************************


# 1.0 Data loading and first exploration
#First, the basic Python packages (more will be loaded later, when needed)

import numpy as np
import pandas as pd

train = pd.read_csv("input/train.csv").set_index("id")
test = pd.read_csv("input/test.csv").set_index("id")

print(train.columns)

print(train.head(5).T)

