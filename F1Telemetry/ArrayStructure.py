#!/usr/bin/env python
# coding=utf-8

#
# F1 Telemetry - Array structure
# Written in Python by Martijn van Kekem
# URL: https://www.vankekem.com/
#
# Creates the array structure where the F1 telemetry data will be saved in
#
# This work was made possible thanks to the following sources:
# -- https://github.com/gmaslowski/f1game-telemetry/wiki/udp-packet-1237-structure
# -- http://forums.codemasters.com/discussion/53139/f1-2017-d-box-and-udp-output-specification
#
# This work is licensed under a "Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License"
# License URL: https://creativecommons.org/licenses/by-nc-nd/4.0/
#

returnData = [] # Create an empty array

# Initialize data array -- BEGIN FUNCTION
def initArray():
    global returnData # Access the global variable returnData
    # FLOATS
    returnData.append(["m_time", 0, 'f']) # Total session time (in seconds)
    returnData.append(["m_lapTime", 0, 'f']) # Current lap time (in seconds)
    returnData.append(["m_lapDistance", 0, 'f']) # Current lap distance (in meters)
    returnData.append(["m_totalDistance", 0, 'f']) # Total distance (in meters)
    returnData.append(["m_x", 0, 'f']) # World space X-position
    returnData.append(["m_y", 0, 'f']) # World space Y-position
    returnData.append(["m_z", 0, 'f']) # World space Z-position
    returnData.append(["m_speed", 0, 'f']) # Car speed in meters per second
    returnData.append(["m_xv", 0, 'f']) # World space X-velocity
    returnData.append(["m_yv", 0, 'f']) # World space Y-velocity
    returnData.append(["m_zv", 0, 'f']) # World space Z-velocity
    returnData.append(["m_xr", 0, 'f']) # World space right X-direction
    returnData.append(["m_yr", 0, 'f']) # World space right Y-direction
    returnData.append(["m_zr", 0, 'f']) # World space right Z-direction
    returnData.append(["m_xd", 0, 'f']) # World space forward X-direction
    returnData.append(["m_yd", 0, 'f']) # World space forward Y-direction
    returnData.append(["m_zd", 0, 'f']) # World space forward Z-direction
    returnData.append(["m_susp_pos_rl", 0, 'f']) # Suspension position - Rear left wheel
    returnData.append(["m_susp_pos_rr", 0, 'f']) # Suspension position - Rear right wheel
    returnData.append(["m_susp_pos_fl", 0, 'f']) # Suspension position - Front left wheel
    returnData.append(["m_susp_pos_fr", 0, 'f']) # Suspension position - Front right wheel
    returnData.append(["m_susp_vel_rl", 0, 'f']) # Suspension velocity - Rear left wheel
    returnData.append(["m_susp_vel_rr", 0, 'f']) # Suspension velocity - Rear right wheel
    returnData.append(["m_susp_vel_fl", 0, 'f']) # Suspension velocity - Front left wheel
    returnData.append(["m_susp_vel_fr", 0, 'f']) # Suspension velocity - Front right wheel
    returnData.append(["m_wheel_speed_rl", 0, 'f']) # Wheel speed - Rear left wheel
    returnData.append(["m_wheel_speed_rr", 0, 'f']) # Wheel speed - Rear right wheel
    returnData.append(["m_wheel_speed_fl", 0, 'f']) # Wheel speed - Front left wheel
    returnData.append(["m_wheel_speed_fr", 0, 'f']) # Wheel speed - Front right wheel
    returnData.append(["m_throttle", 0, 'f']) # Throttle value (min: 0, max: 1)
    returnData.append(["m_steer", 0, 'f']) # Steering rotation (min: 1, max: -1)
    returnData.append(["m_brake", 0, 'f']) # Brake value (min: 0, max: 1)
    returnData.append(["m_clutch", 0, 'f']) # Clutch value (min: 0, max: 1)
    returnData.append(["m_gear", 0, 'f']) # Current gear (0 => R, 1 => N, 2 => ...)
    returnData.append(["m_gforce_lat", 0, 'f']) # G-Force latitude
    returnData.append(["m_gforce_lon", 0, 'f']) # G-Force longitude
    returnData.append(["m_lap", 0, 'f']) # Current lap
    returnData.append(["m_engineRate", 0, 'f']) # Current RPM
    returnData.append(["m_sli_pro_native_support", 0, 'f']) # SLI Pro support
    returnData.append(["m_car_position", 0, 'f']) # Car race position
    returnData.append(["m_kers_level", 0, 'f']) # KERS energy left
    returnData.append(["m_kers_max_level", 0, 'f']) # KERS maximum energy
    returnData.append(["m_drs", 0, 'f']) # DRS state, 0 = off, 1 = on
    returnData.append(["m_traction_control", 0, 'f']) # Traction control enabled (off: 0, high: 2)
    returnData.append(["m_anti_lock_brakes", 0, 'f']) # Anti lock brakes enabled (off: 0, on: 1)
    returnData.append(["m_fuel_in_tank", 0, 'f']) # Current fuel mass
    returnData.append(["m_fuel_capacity", 0, 'f']) # Fuel capacity
    returnData.append(["m_in_pits", 0, 'f']) # Car in pit (0: no, 1: pitting, 2: in pit area)
    returnData.append(["m_sector", 0, 'f']) # Current sector car is in (0: sector 1, 1: sector 2, 2: sector 3)
    returnData.append(["m_sector1_time", 0, 'f']) # Current first sector time
    returnData.append(["m_sector2_time", 0, 'f']) # Current second sector time
    returnData.append(["m_brakes_temp_rl", 0, 'f']) # Brake temperature - Rear left wheel
    returnData.append(["m_brakes_temp_rr", 0, 'f']) # Brake temperature - Rear right wheel
    returnData.append(["m_brakes_temp_fl", 0, 'f']) # Brake temperature - Front left wheel
    returnData.append(["m_brakes_temp_fr", 0, 'f']) # Brake temperature - Front right wheel
    returnData.append(["m_tyres_pressure_rl", 0, 'f']) # Tyre pressure - Rear left wheel
    returnData.append(["m_tyres_pressure_rr", 0, 'f']) # Tyre pressure - Rear right wheel
    returnData.append(["m_tyres_pressure_fl", 0, 'f']) # Tyre pressure - Front left wheel
    returnData.append(["m_tyres_pressure_fr", 0, 'f']) # Tyre pressure - Front right wheel
    # Player's team - Modern teams: (0: Red-Bull, 1: Ferrari, 2: McLaren, 3: Renault, 4: Mercedes, ...
    # ... 5: Sauber, 6: Force India, 7: Williams, 8: Toro Rosso, 11: Haas)
    # Player's team - Classic teams: (0: Williams 1992, 1: McLaren 1988, 2: McLaren 2008, 3: Ferrari 2004, 4: Ferrari 1995, ...
    # ... 5: Ferrari 2007, 6: McLaren 1998, 7: Williams 1996, 8: Renault 2006, 10: Ferrar 2002, 11: Red Bull 2010, 12: McLaren 1991)
    returnData.append(["m_team_info", 0, 'f'])
    returnData.append(["m_total_laps", 0, 'f']) # Total amount of laps in this race
    returnData.append(["m_track_size", 0, 'f']) # Track size (in meters)
    returnData.append(["m_last_lap_time", 0, 'f']) # Last lap time (in seconds)
    returnData.append(["m_max_rpm", 0, 'f']) # Maximum RPM, point where rev limiter will kick in
    returnData.append(["m_idle_rpm", 0, 'f']) # Idle RPM
    returnData.append(["m_max_gears", 0, 'f']) # Total amount of gears on the car
    returnData.append(["m_sessionType", 0, 'f']) # Session type (0: unknown, 1: practice, 2: qualifying, 3: race)
    returnData.append(["m_drsAllowed", 0, 'f']) # DRS allowed (0: not allowed, 1: allowed, -1: invalid/unknown) -- returns 0 if DRS is enabled
    # Track number (-1: unknown, 0: Melbourne, 1: Sepang, 2: Shanghai, 3: Bahrain, 4: Catalunya, ...
    # ... 5: Monaco, 6: Montreal, 7: Silverstone, 8: Hockenheim, 9: Hungaroring, 10: Spa, 11: Monza, ...
    # ... 12: Singapore, 13: Suzuka, 14: Abu Dhabi, 15: Texas, 16: Brazil, 17: Austria, 18: Sochi, 19: Mexico, ...
    # ... 20: Baku, 21: Sakir Short, 22: Silverstone short, 23: Texas Short, 24: Suzuka Short)
    returnData.append(["m_track_number", 0, 'f'])
    returnData.append(["m_vehicleFIAFlags", 0, 'f']) # Race flags (-1: invalid/unknown, 0: none, 1: green, 2: blue, 3: yellow, 4: red)
    returnData.append(["m_era", 0, 'f']) # ERA, (modern: 2017, classic: 1980)
    returnData.append(["m_engine_temperature", 0, 'f']) # Temperature of the engine
    returnData.append(["m_gforce_vert", 0, 'f']) # Vertical G-force
    returnData.append(["m_ang_vel_x", 0, 'f']) # Angular X-velocity
    returnData.append(["m_ang_vel_y", 0, 'f']) # Angular Y-velocity
    returnData.append(["m_ang_vel_z", 0, 'f']) # Angular Z-velocity
    # BYTES
    returnData.append(["m_tyres_temperature_rl", 0, 'b']) # Tyre temperature - Rear left tyre
    returnData.append(["m_tyres_temperature_rr", 0, 'b']) # Tyre temperature - Rear right tyre
    returnData.append(["m_tyres_temperature_fl", 0, 'b']) # Tyre temperature - Front left tyre
    returnData.append(["m_tyres_temperature_fr", 0, 'b']) # Tyre temperature - Front right tyre
    returnData.append(["m_tyres_wear_rl", 0, 'b']) # Tyre wear - Rear left tyre
    returnData.append(["m_tyres_wear_rr", 0, 'b']) # Tyre wear - Rear right tyre
    returnData.append(["m_tyres_wear_fl", 0, 'b']) # Tyre wear - Front left tyre
    returnData.append(["m_tyres_wear_fr", 0, 'b']) # Tyre wear - Front right tyre
    returnData.append(["m_tyre_compound", 0, 'b']) # Tyre compound (0: ultrasoft, 1: supersoft, 2: soft, 3: medium, 4: hard, 5: inter, 6: wet)
    returnData.append(["m_front_brake_bias", 0, 'b']) # Front brake bias (percentage)
    returnData.append(["m_fuel_mix", 0, 'b']) # Fuel mix (0: lean, 1: standard, 2: rich, 3: max)
    returnData.append(["m_currentLapInvalid", 0, 'b']) # If the current lap is invalid (0: valid, 1: invalid)
    returnData.append(["m_tyres_damage_rl", 0, 'b']) # Tyre damamge including wear - Rear left tyre
    returnData.append(["m_tyres_damage_rr", 0, 'b']) # Tyre damamge including wear - Rear right tyre
    returnData.append(["m_tyres_damage_fl", 0, 'b']) # Tyre damamge including wear - Front left tyre
    returnData.append(["m_tyres_damage_fr", 0, 'b']) # Tyre damamge including wear - Front right tyre
    returnData.append(["m_front_left_wing_damage", 0, 'b']) # Left front wing damage (percentage)
    returnData.append(["m_front_right_wing_damage", 0, 'b']) # Right front wing damage (percentage)
    returnData.append(["m_rear_wing_damage", 0, 'b']) # Rear wing damage (percentage)
    returnData.append(["m_engine_damage", 0, 'b']) # Engine damage (percentage)
    returnData.append(["m_gear_box_damage", 0, 'b']) # Gearbox dmaage (percentage)
    returnData.append(["m_exhaust_damage", 0, 'b']) # Exhaust damage (percentage)
    returnData.append(["m_pit_limiter_status", 0, 'b']) # Pit limiter status (0: disabled, 1: enabled)
    returnData.append(["m_pit_speed_limit", 0, 'b']) # Maximum speed in the pit lane
    # FLOATS
    returnData.append(["m_session_time_left", 0, 'f']) # Remaining session time (in seconds)
    # BYTES
    returnData.append(["m_rev_lights_percent", 0, 'b']) # Rev lights percentage
    returnData.append(["m_is_spectating", 0, 'b']) # Whether the player is spectating
    returnData.append(["m_spectator_car_index", 0, 'b']) # Car index of the spectating player
    returnData.append(["m_num_cars", 0, 'b']) # Number of cars in total
    returnData.append(["m_player_car_index", 0, 'b']) # Car index of the current player

    # Create objects for 20 cars
    for car in range(0, 20):
        # FLOATS
        returnData.append(["car_"+str(car)+"_m_worldPosition_x", 0, 'f']) # World X-coordinate of car
        returnData.append(["car_"+str(car)+"_m_worldPosition_y", 0, 'f']) # World Y-coordinate of car
        returnData.append(["car_"+str(car)+"_m_worldPosition_z", 0, 'f']) # World Z-coordinate of car
        returnData.append(["car_"+str(car)+"_m_lastLapTime", 0, 'f']) # Last lap time (in seconds)
        returnData.append(["car_"+str(car)+"_m_currentLapTime", 0, 'f']) # Current lap time (in seconds)
        returnData.append(["car_"+str(car)+"_m_bestLapTime", 0, 'f']) # Fastest lap time (in seconds)
        returnData.append(["car_"+str(car)+"_m_sector1Time", 0, 'f']) # Sector 1 time
        returnData.append(["car_"+str(car)+"_m_sector2Time", 0, 'f']) # Sector 2 time
        returnData.append(["car_"+str(car)+"_m_lapDistance", 0, 'f']) # Distance traveled in current lap (in meters)
        # BYTES
        # Current driver - Modern drivers (9: Hamilton, 15: Bottas, 16: Ricciardo, 22: Verstappen, 0: Vettel, 6: Räikkönen, 5: Perez, ...
        # ... 33: Ocon, 3: Massa, 35: Stroll, 2: Alonso, 34: Vandoorne, 23: Sainz Jr., 1: Kvyat, 7: Grosjean, 14: Magnussen, ...
        # ... 10: Hulkenberg, 20: Palmer, 18: Ericsson, 31: Wehrlein)
        # Current driver - Classic drivers (23: Barnes, 1: Giles, 16: Murray, 68: Roth, 2: Correia, 3: Levasseur, 24: Schiffer, ...
        # ... 4: Forest, 20: Letourneau, 6: Saari, 9: Atiyeh, 18: Calabresi, 22: Izum, 10: Clarke, 8: Kaufmann, 14: Laursen, ...
        # ... 31: Nieves, 7: Belousov, 0: Michalski, 5: Monero, 15: Coppens, 32: Visser, 33: Waldmuller, 34: Quesada)
        returnData.append(["car_"+str(car)+"_m_driverId", 0, 'b'])
        returnData.append(["car_"+str(car)+"_m_teamId", 0, 'b']) # Team of car. See line 79
        returnData.append(["car_"+str(car)+"_m_carPosition", 0, 'b']) # Track position of vehicle
        returnData.append(["car_"+str(car)+"_m_currentLapNum", 0, 'b']) # Current lap the player is in
        returnData.append(["car_"+str(car)+"_m_tyreCompound", 0, 'b']) # Tyre compound. See line 113
        returnData.append(["car_"+str(car)+"_m_inPits", 0, 'b']) # Wheter the car is in the pits. See line 67
        returnData.append(["car_"+str(car)+"_m_sector", 0, 'b']) # Current sector the car is in. See line 68
        returnData.append(["car_"+str(car)+"_m_currentLapInvalid", 0, 'b']) # Wheter the current lap is invalid. See line 116
        returnData.append(["car_"+str(car)+"_m_penalties", 0, 'b']) # Sum of all time penalties (in seconds)

    # FLOATS
    returnData.append(["m_yaw", 0, 'f']) # Angle between moving point and facing point of the car over the Z-axis
    returnData.append(["m_pitch", 0, 'f']) # Angle between moving point and facing point of the car over the Y-axis
    returnData.append(["m_roll", 0, 'f']) # Angle between moving point and facing point of the car over the X-axis
    returnData.append(["m_x_local_velocity", 0, 'f']) # X-velocity in local space
    returnData.append(["m_y_local_velocity", 0, 'f']) # Y-velocity in local space
    returnData.append(["m_z_local_velocity", 0, 'f']) # Z-velocity in local space
    returnData.append(["m_susp_acceleration_rl", 0, 'f']) # Suspension acceleration - Rear left wheel
    returnData.append(["m_susp_acceleration_rr", 0, 'f']) # Suspension acceleration - Rear right wheel
    returnData.append(["m_susp_acceleration_fl", 0, 'f']) # Suspension acceleration - Front left wheel
    returnData.append(["m_susp_acceleration_fr", 0, 'f']) # Suspension acceleration - Front right wheel
    returnData.append(["m_ang_acc_x", 0, 'f']) # Angular X-acceleration
    returnData.append(["m_ang_acc_y", 0, 'f']) # Angular Y-acceleration
    returnData.append(["m_ang_acc_z", 0, 'f']) # Angular Z-acceleration
# Initialize data array -- END FUNCTION

initArray() # Execute the function
