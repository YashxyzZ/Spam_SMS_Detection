import train_model
import predict

print("\n=== Spam SMS Detection ===")

# Allow user to input a message for testing
while True:
    user_input = input("\nEnter an SMS message (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    result = predict.predict_sms(user_input)
    print(f"Prediction: {result}")
