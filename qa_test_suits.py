# qa_test_suite.py

from main import get_structured_output
import traceback

# Define a list of test cases with expected intents
TEST_CASES = [
    {
        "input": "write an essay on democracy",
        "expected_intent": "write_essay"
    },
    {
        "input": "create a telegram bot that reminds me to drink water every hour",
        "expected_intent": "build_bot"
    },
    {
        "input": "i want a script that emails me my crypto prices every evening",
        "expected_intent": "build_script"
    },
    {
        "input": "generate a README for a project on machine learning",
        "expected_intent": "create_documentation"
    },
    {
        "input": "write a thank you email to my manager",
        "expected_intent": "send_email"
    },
    {
        "input": "summarize the history of the roman empire in 100 words",
        "expected_intent": "summarize_information"
    },
    {
        "input": "analyze my excel file for duplicate rows",
        "expected_intent": "analyze_file"
    },
    {
        "input": "build a portfolio website for a designer",
        "expected_intent": "build_website"
    },
    {
        "input": "onboarding document for summer interns",
        "expected_intent": "create_documentation"
    },
    {
        "input": "generate a python script to scrape trending videos on YouTube",
        "expected_intent": "scrape_data"
    }
]

def run_tests():
    passed = 0
    failed = 0

    print("\n🔬 Running QA Test Suite\n" + "-" * 40)

    for i, test in enumerate(TEST_CASES, start=1):
        print(f"Test {i}: \"{test['input']}\"")
        try:
            result = get_structured_output(test["input"])
            intent = result.get("intent", "None")
            if intent == test["expected_intent"]:
                print(f"✅ PASS — Intent: {intent}\n")
                passed += 1
            else:
                print(f"❌ FAIL — Expected: {test['expected_intent']}, Got: {intent}\n")
                failed += 1
        except Exception as e:
            print(f"❌ ERROR — Exception occurred: {e}")
            traceback.print_exc()
            failed += 1

    print("🧪 TEST SUMMARY")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print("-" * 40)

if __name__ == "__main__":
    run_tests()
