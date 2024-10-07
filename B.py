numbers = ["1234xxxx"] * 50  # ৫০ বার "1234xxxx" এর তালিকা তৈরি
start_numbers = range(6567, 6617)  # ৫০টি ভিন্ন সংখ্যা 6567 থেকে শুরু করে
new_numbers = [number.replace("xxxx", str(num)) for number, num in zip(numbers, start_numbers)]
print(new_numbers)
