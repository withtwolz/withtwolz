#!/usr/bin/env python3
"""
Resume Keyword Scanner
Scans your resume text for target keywords and generates a tracking table.
Usage: python keyword_scanner.py resume.txt
"""

import re
import sys
from typing import Dict, List, Tuple

# ANSI color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'  # Reset to default color

class ResumeKeywordScanner:
    def __init__(self):
        # Define target keywords based on job descriptions analysis
        self.target_keywords = {
            # HIGH PRIORITY - Appears in 60%+ of jobs
            'HIGH': [
                'TypeScript', 'Cypress', 'Playwright', 'API testing', 
                'Test automation', 'Automated testing', 'End-to-end testing',
                'Cross-functional', 'Test strategy', 'Test plans', 'CI/CD',
                'Quality engineering', 'Technical leadership', 'SDLC integration'
            ],
            
            # MEDIUM PRIORITY - Appears in 40%+ of jobs  
            'MED': [
                'Regression testing', 'Integration testing', 'Performance testing',
                'Load testing', 'Cross-browser testing', 'Mobile testing', 'Agile',
                'Test case management', 'Defect tracking', 'Test coverage',
                'Release management', 'Continuous testing', 'Stakeholder collaboration',
                'Mentoring', 'REST API', 'GraphQL'
            ],
            
            # LOW PRIORITY - Still valuable but less critical
            'LOW': [
                'JIRA', 'TestRail', 'React Testing Library', 'Selenium',
                'Python', 'JavaScript', 'Docker', 'Kubernetes', 'AWS',
                'GitHub Actions', 'Jenkins', 'Postman'
            ]
        }
        
        # Flatten all keywords for easy searching
        self.all_keywords = []
        for priority_keywords in self.target_keywords.values():
            self.all_keywords.extend(priority_keywords)
    
    def load_resume(self, file_path: str) -> str:
        """Load resume text from file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)
    
    def scan_keywords(self, resume_text: str) -> Dict[str, bool]:
        """Scan resume text for target keywords."""
        results = {}
        
        # Convert resume to lowercase for case-insensitive matching
        resume_lower = resume_text.lower()
        
        for keyword in self.all_keywords:
            # Create regex pattern for whole word matching
            pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
            found = bool(re.search(pattern, resume_lower))
            results[keyword] = found
            
        return results
    
    def get_keyword_priority(self, keyword: str) -> str:
        """Get the priority level of a keyword."""
        for priority, keywords in self.target_keywords.items():
            if keyword in keywords:
                return priority
        return 'UNKNOWN'
    
    def generate_report(self, keyword_results: Dict[str, bool]) -> None:
        """Generate and print the keyword tracking report."""
        print(f"{Colors.BOLD}{Colors.BLUE}RESUME KEYWORD ANALYSIS REPORT{Colors.END}")
        print("=" * 80)
        print(f"{'Keyword':<26} | {'Priority':<8} | {'Status':<10} | {'Found'}")
        print("-" * 80)
        
        # Count statistics
        found_count = 0
        total_count = len(self.all_keywords)
        priority_stats = {'HIGH': [0, 0], 'MED': [0, 0], 'LOW': [0, 0]}
        
        # Sort keywords by priority and then alphabetically
        sorted_keywords = []
        for priority in ['HIGH', 'MED', 'LOW']:
            keywords = sorted(self.target_keywords[priority])
            sorted_keywords.extend(keywords)
        
        for keyword in sorted_keywords:
            found = keyword_results.get(keyword, False)
            priority = self.get_keyword_priority(keyword)
            
            if found:
                status = f"{Colors.GREEN}{Colors.BOLD}✓{Colors.END}"
                keyword_display = f"{Colors.GREEN}{keyword}{Colors.END}"
            else:
                status = f"{Colors.RED}{Colors.BOLD}X{Colors.END}"
                keyword_display = keyword
            
            print(f"{keyword_display:<35} | {priority:<8} | {status:<20} | {found}")
            
            # Update statistics
            if found:
                found_count += 1
            priority_stats[priority][1] += 1  # total for this priority
            if found:
                priority_stats[priority][0] += 1  # found for this priority
        
        # Print summary statistics
        print("\n" + "=" * 80)
        print(f"{Colors.BOLD}{Colors.BLUE}SUMMARY STATISTICS:{Colors.END}")
        
        overall_percentage = found_count/total_count*100
        if overall_percentage >= 70:
            overall_color = Colors.GREEN
        elif overall_percentage >= 50:
            overall_color = Colors.YELLOW
        else:
            overall_color = Colors.RED
            
        print(f"Overall Coverage: {overall_color}{Colors.BOLD}{found_count}/{total_count} keywords ({overall_percentage:.1f}%){Colors.END}")
        
        for priority in ['HIGH', 'MED', 'LOW']:
            found, total = priority_stats[priority]
            percentage = found/total*100 if total > 0 else 0
            
            if percentage >= 80:
                color = Colors.GREEN
            elif percentage >= 60:
                color = Colors.YELLOW
            else:
                color = Colors.RED
                
            print(f"{priority} Priority: {color}{found}/{total} keywords ({percentage:.1f}%){Colors.END}")
        
        # Recommendations
        print("\n" + "=" * 80)
        print(f"{Colors.BOLD}{Colors.BLUE}RECOMMENDATIONS:{Colors.END}")
        
        missing_high = [k for k in self.target_keywords['HIGH'] if not keyword_results.get(k, False)]
        if missing_high:
            print(f"{Colors.RED}{Colors.BOLD}Missing HIGH priority keywords (add these first):{Colors.END}")
            for keyword in missing_high[:5]:  # Show top 5
                print(f"  {Colors.RED}• {keyword}{Colors.END}")
        
        missing_med = [k for k in self.target_keywords['MED'] if not keyword_results.get(k, False)]
        if missing_med:
            print(f"{Colors.YELLOW}{Colors.BOLD}Missing MEDIUM priority keywords (add when possible):{Colors.END}")
            for keyword in missing_med[:3]:  # Show top 3
                print(f"  {Colors.YELLOW}• {keyword}{Colors.END}")
                
        if found_count/total_count >= 0.8:
            print(f"\n{Colors.GREEN}{Colors.BOLD}🎯 EXCELLENT! Your resume has strong keyword coverage for ATS systems.{Colors.END}")
        elif found_count/total_count >= 0.6:
            print(f"\n{Colors.YELLOW}{Colors.BOLD}👍 GOOD progress! Focus on HIGH priority keywords to reach 80%+ coverage.{Colors.END}")
        else:
            print(f"\n{Colors.RED}{Colors.BOLD}⚠️  NEEDS WORK! Add HIGH priority keywords to improve ATS compatibility.{Colors.END}")
    
    def export_csv(self, keyword_results: Dict[str, bool], output_file: str = "keyword_results.csv") -> None:
        """Export results to CSV file."""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("Keyword,Priority,Found,Status\n")
                for keyword in self.all_keywords:
                    found = keyword_results.get(keyword, False)
                    priority = self.get_keyword_priority(keyword)
                    status = "✓" if found else "✗"
                    f.write(f'"{keyword}",{priority},{found},{status}\n')
            print(f"\nResults exported to: {output_file}")
        except Exception as e:
            print(f"Error exporting CSV: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python keyword_scanner.py <resume_file.txt>")
        print("Example: python keyword_scanner.py my_resume.txt")
        sys.exit(1)
    
    resume_file = sys.argv[1]
    create_csv = sys.argv[2] if len(sys.argv) > 2 else False
    scanner = ResumeKeywordScanner()
    
    # Load and scan resume
    print(f"Scanning resume: {resume_file}")
    resume_text = scanner.load_resume(resume_file)
    keyword_results = scanner.scan_keywords(resume_text)
    
    # Generate report
    scanner.generate_report(keyword_results)
    
    # Export to CSV (optional)
    if create_csv:
        scanner.export_csv(keyword_results)
    
    print(f"\nScan complete! Found keywords will help your resume pass ATS systems.")

if __name__ == "__main__":
    main()
