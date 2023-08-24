# Create the class BestRouteAnalyzer and initialize it with the parameters location_a and location_b 
class BestRouteAnalyzer:
    def __init__(self, location_a, location_b ):
        self.location_a = location_a
        self.location_b = location_b
# Define the method or  function that takes two parameters speed_of_machine and distance_between_ab and return expected_time 
    def calculate_expected_time(self, speed_of_machine, distance_between_ab):
        expected_time = distance_between_ab / speed_of_machine
        print(expected_time)
        return expected_time

# The function checks for obstruction by comparing the two parameters, actual_time and expected_time, and returns True		
    def check_obstruction(self, actual_time, expected_time):
        if actual_time > expected_time:
	        return True  
        return False

#  This method checks for obstruction that is impenetrable by comparing the  difference two parameters(actual_time and expected_time) against threashold time , and returns True
    def check_obstruction_impenetrable(self, actual_time, expected_time):
        time_difference = actual_time - expected_time 
        if time_difference > 60:
	        return True  
        return False

# Example usage
if __name__ == "__main__":
    # Simulated values for the actual time and the speed of the machine
    actual_time = 78  # Simulated actual time in minutes
    speed_of_machine = 10  # Simulated machine speed in miles per minute
        
    # Distance between Point A and Point B (simulated)
    distance_between_ab = 152  # Simulated distance in miles


    # Creating an instance of the BestRouteAnalyzer class
    
    detector = BestRouteAnalyzer('PointA' , 'PointB')
    expected_time = detector.calculate_expected_time(speed_of_machine , distance_between_ab)

    # Detecting obstruction
    is_obstruction = detector.check_obstruction(actual_time, expected_time)  

    # Detecting impenetrable obstruction 
    is_obstruction_impenetrable = detector.check_obstruction_impenetrable(actual_time, expected_time)
    
    if is_obstruction:
        print(f"There is an obstruction between {detector.location_a} and {detector.location_b}.")

        if is_obstruction_impenetrable:
           print("The obstruction is impenetrable.")
    
    else:
        print(f"No obstruction detected between {detector.location_a} and {detector.location_b}.")

  