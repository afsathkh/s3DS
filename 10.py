import numpy as np
nums = np.arange(16,dtype="int").reshape(-1,4)
print("Orginal array:")
print(nums)
print("\n New array after swping first and last row of the said array:")
nums=nums[[-1,1,2,0]]
print(nums)