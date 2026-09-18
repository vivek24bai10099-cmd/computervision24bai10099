import argparse
from src.pipeline import process_image, process_webcam

def main():
    parser = argparse.ArgumentParser(description="Hand Gesture Counter")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--image", help="Path to a hand image")
    group.add_argument("--webcam", action="store_true", help="Run webcam mode")
    args = parser.parse_args()

    if args.image:
        result = process_image(args.image)
        print("\nHand Gesture Counter")
        print(f"Hands detected: {result['hands']}")
        print(f"Raised fingers: {result['fingers']}")
        print(f"Gesture: {result['gesture']}")
        print("Result saved to output/annotated_result.jpg")
    else:
        process_webcam()

if __name__ == "__main__":
    main()
