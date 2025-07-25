#!/usr/bin/env python3
"""
YAJPH Demo: Prove the anti-black-box engine works
"""

from yajph import Router
import json

def demo_loan_approval():
    """Demo 1: Loan approval with explainable rejection"""
    print("🏦 LOAN APPROVAL DEMO")
    print("=" * 40)
    
    # Define rules
    rules = {
        'requirements': {
            'credit_score': 680,
            'dti': '43%',
            'income': 50000
        },
        'must_have': ['bank_account', 'employment_verification']
    }
    
    # Test bad applicant
    bad_applicant = {
        'credit_score': 620,  # too low
        'dti': '47%',         # too high
        'income': 45000,      # too low
        'bank_account': True,
        # missing employment_verification
    }
    
    router = Router(rules=rules)
    result = router.evaluate(bad_applicant)
    
    print("❌ REJECTION (with explanation):")
    print(json.dumps({
        'passed': result.passed,
        'rejected_on': result.rejected_on,
        'your_score': result.your_score,
        'threshold': result.threshold,
        'fix': result.fix
    }, indent=2))
    
    print("\n" + "=" * 40)
    
    # Test good applicant
    good_applicant = {
        'credit_score': 720,
        'dti': '38%',
        'income': 75000,
        'bank_account': True,
        'employment_verification': True
    }
    
    result = router.evaluate(good_applicant)
    print("✅ APPROVAL:")
    print(json.dumps({
        'passed': result.passed,
        'fix': result.fix
    }, indent=2))


def demo_hiring():
    """Demo 2: Job candidate screening"""
    print("\n\n💼 HIRING DEMO")
    print("=" * 40)
    
    rules = {
        'requirements': {
            'python': 3,  # out of 5
            'sql': 4,     # out of 5
        },
        'must_have': ['portfolio']
    }
    
    # Weak candidate
    weak_candidate = {
        'python': '2/5',  # too low
        'sql': '2/5',     # too low
        'portfolio': 'github.com/user/projects'
    }
    
    router = Router(rules=rules)
    result = router.evaluate(weak_candidate)
    
    print("❌ REJECTION (with growth path):")
    print(json.dumps({
        'passed': result.passed,
        'missing': result.missing,
        'resources': result.resources,
        'fix': result.fix
    }, indent=2))


def demo_simple_api():
    """Demo 3: Show the simple API"""
    print("\n\n🚀 SIMPLE API DEMO")
    print("=" * 40)
    
    from yajph import Router
    
    # One-liner setup
    router = Router(rules={
        'requirements': {'age': 18},
        'must_have': ['id']
    })
    
    # One-liner evaluation
    result = router.evaluate({'age': 16, 'id': True})
    
    print("Code:")
    print("router = Router(rules={'requirements': {'age': 18}})")
    print("result = router.evaluate({'age': 16})")
    print(f"\nResult: {result.passed} - {result.fix}")


if __name__ == "__main__":
    demo_loan_approval()
    demo_hiring() 
    demo_simple_api()
    
    print("\n" + "=" * 50)
    print("🎉 YAJPH: Every 'no' comes with a roadmap to 'yes'")
    print("⭐ Star this repo if you believe systems should explain themselves")
