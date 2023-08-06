# Car Price Prediction

## Dataset
### Features

1. **Brand**: The brand of the car (string).

2. **Model**: The model name of the car (string).

3. **Year**: The manufacturing year of the car (float).

4. **Mileage**: The mileage of the car (float).

5. **Engine**: The type of engine in the car (string).

6. **Engine Size**: The size of the car's engine (float).

7. **Transmission**: The type of transmission (string).

8. **Automatic Transmission**: Indicator of whether the car has an automatic transmission (float).

9. **Fuel Type**: The type of fuel the car uses (string).

10. **Drivetrain**: The type of drivetrain (string).

11. **Min MPG**: The minimum miles per gallon the car can achieve (float).

12. **Max MPG**: The maximum miles per gallon the car can achieve (float).

13. **Damaged**: Indicator of whether the car has any damage (float).

14. **First Owner**: Indicator of whether the car is owned by the first owner (float).

15. **Personal Using**: Indicator of whether the car is used for personal purposes (float).

16. **Turbo**: Indicator of whether the car has a turbocharger (float).

17. **Alloy Wheels**: Indicator of whether the car has alloy wheels (float).

18. **Adaptive Cruise Control**: Indicator of whether the car has adaptive cruise control (float).

19. **Navigation System**: Indicator of whether the car has a navigation system (float).

20. **Power Liftgate**: Indicator of whether the car has a power liftgate (float).

21. **Backup Camera**: Indicator of whether the car has a backup camera (float).

22. **Keyless Start**: Indicator of whether the car has keyless start (float).

23. **Remote Start**: Indicator of whether the car has remote start (float).

24. **Sunroof/Moonroof**: Indicator of whether the car has a sunroof or moonroof (float).

25. **Automatic Emergency Braking**: Indicator of whether the car has automatic emergency braking (float).

26. **Stability Control**: Indicator of whether the car has stability control (float).

27. **Leather Seats**: Indicator of whether the car has leather seats (float).

28. **Memory Seat**: Indicator of whether the car has memory seats (float).

29. **Third Row Seating**: Indicator of whether the car has third-row seating (float).

30. **Apple CarPlay/Android Auto**: Indicator of whether the car supports Apple CarPlay or Android Auto (float).

31. **Bluetooth**: Indicator of whether the car has Bluetooth connectivity (float).

32. **USB Port**: Indicator of whether the car has a USB port (float).

33. **Heated Seats**: Indicator of whether the car has heated seats (float).

34. **Interior Color**: The color of the car's interior (string).

35. **Exterior Color**: The color of the car's exterior (string).

## Notebook && Pipeline consists of experimetal and actual pipeline of code respectively.

## To fire-up the api run:
```
docker build -t car_price_prediction . 
```

## To run server:
```
docker run -d -p 80:80 car_price_prediction
```


# **Congratulations**, *your api is running at port no. 80 on local server*