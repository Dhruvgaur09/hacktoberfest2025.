numbers = [10, 20, -5, 30, -1, 50]

errors = [num for num in numbers if num < 0]

if errors:
    print("❌ Error: Negative numbers found:", errors)
else:
    print("✅ No errors found")
