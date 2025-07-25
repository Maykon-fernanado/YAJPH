"""
YAJPH: The Anti-Black-Box Engine
GitHub's First Explainable Decision Framework

Every "no" comes with a roadmap to "yes".
"""

import yaml
import json
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict


@dataclass
class Decision:
    """The explainable decision result"""
    passed: bool
    score: Optional[float] = None
    missing: Dict[str, str] = None
    rejected_on: Optional[str] = None
    your_score: Optional[Any] = None
    threshold: Optional[Any] = None
    fix: Optional[str] = None
    resources: List[str] = None
    audit_trail: List[str] = None
    
    def __post_init__(self):
        if self.missing is None:
            self.missing = {}
        if self.resources is None:
            self.resources = []
        if self.audit_trail is None:
            self.audit_trail = []


class Router:
    """The core YAJPH reasoning engine"""
    
    def __init__(self, input_schema: str = None, output_schema: str = None, 
                 rules: Dict[str, Any] = None, models: Dict[str, str] = None):
        self.input_schema = input_schema
        self.output_schema = output_schema
        self.rules = rules or {}
        self.models = models or {}
        
        # Load rules from YAML if provided
        if input_schema and input_schema.endswith('.yaml'):
            with open(input_schema, 'r') as f:
                self.rules = yaml.safe_load(f)
    
    def evaluate(self, data: Dict[str, Any]) -> Decision:
        """
        The magic happens here: transparent, explainable decisions
        """
        audit_trail = [f"evaluating: {list(data.keys())}"]
        
        # Check each rule
        for rule_name, threshold in self.rules.get('requirements', {}).items():
            audit_trail.append(f"checking: {rule_name}")
            
            if rule_name not in data:
                return Decision(
                    passed=False,
                    missing={rule_name: f"required but not provided"},
                    rejected_on=rule_name,
                    audit_trail=audit_trail,
                    fix=f"Please provide {rule_name} information"
                )
            
            user_value = data[rule_name]
            
            # Handle different comparison types
            if isinstance(threshold, str) and threshold.endswith('%'):
                # DTI percentage check
                threshold_val = float(threshold.rstrip('%'))
                user_val = float(str(user_value).rstrip('%'))
                
                if user_val > threshold_val:
                    return Decision(
                        passed=False,
                        rejected_on=rule_name,
                        your_score=f"{user_val}%",
                        threshold=threshold,
                        audit_trail=audit_trail,
                        fix=f"Reduce {rule_name} to below {threshold}"
                    )
            
            elif isinstance(threshold, (int, float)):
                # Numeric threshold (like credit score or skill level)
                if isinstance(user_value, str) and '/' in user_value:
                    # Handle "2/5" format
                    user_val = float(user_value.split('/')[0])
                else:
                    user_val = float(user_value)
                
                if user_val < threshold:
                    return Decision(
                        passed=False,
                        rejected_on=rule_name,
                        your_score=user_value,
                        threshold=threshold,
                        missing={rule_name: f"{user_value} (need {threshold})"},
                        audit_trail=audit_trail,
                        resources=self._get_resources(rule_name),
                        fix=f"Improve {rule_name} to at least {threshold}"
                    )
        
        # Check required items
        for required_item in self.rules.get('must_have', []):
            if required_item not in data or not data[required_item]:
                return Decision(
                    passed=False,
                    rejected_on=required_item,
                    missing={required_item: "required but missing"},
                    audit_trail=audit_trail,
                    fix=f"Please provide {required_item}"
                )
        
        # All checks passed!
        audit_trail.append("all_checks_passed")
        return Decision(
            passed=True,
            audit_trail=audit_trail,
            fix="No action needed - you qualify!"
        )
    
    def _get_resources(self, skill: str) -> List[str]:
        """Suggest helpful resources for improvement"""
        resources_map = {
            'sql': ['https://sqlzoo.net', 'https://w3schools.com/sql'],
            'python': ['https://python.org/tutorial', 'https://codecademy.com/python'],
            'credit_score': ['https://creditkarma.com', 'https://annualcreditreport.com']
        }
        return resources_map.get(skill.lower(), [])


def attach_router(input_schema: str, output_schema: str, 
                 llm_router=None) -> Router:
    """
    Attach YAJPH to your existing application
    """
    return Router(input_schema=input_schema, output_schema=output_schema)


def evaluate_yaml(rules_file: str, data_file: str) -> Dict[str, Any]:
    """
    CLI-friendly function for YAML-to-JSON evaluation
    """
    # Load rules
    with open(rules_file, 'r') as f:
        rules = yaml.safe_load(f)
    
    # Load data
    with open(data_file, 'r') as f:
        if data_file.endswith('.yaml') or data_file.endswith('.yml'):
            data = yaml.safe_load(f)
        else:
            data = json.load(f)
    
    # Create router and evaluate
    router = Router(rules=rules)
    result = router.evaluate(data)
    
    return asdict(result)


def deploy(input_schema: str, output_schema: str, api_mode: str = "rest", port: int = 8080):
    """
    Deploy YAJPH as a web service (placeholder for now)
    """
    print(f"🚀 YAJPH would deploy on port {port}")
    print(f"📄 Input schema: {input_schema}")
    print(f"📄 Output schema: {output_schema}")
    print(f"🌐 Mode: {api_mode}")
    print("(Full deployment coming in v0.2)")


# CLI entry point
def main():
    """Simple CLI for testing"""
    import argparse
    parser = argparse.ArgumentParser(description="YAJPH: The Anti-Black-Box Engine")
    parser.add_argument('--rules', required=True, help='YAML rules file')
    parser.add_argument('--input', required=True, help='Input data file')
    parser.add_argument('--output', help='Output JSON file (optional)')
    
    args = parser.parse_args()
    
    result = evaluate_yaml(args.rules, args.input)
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)
    else:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
