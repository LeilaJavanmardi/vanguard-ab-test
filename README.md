### Vanguard Digital Experiment Analysis - AB test

Welcome to the Vanguard Digital Experiment Analysis repository! This project analyzes the results of a digital experiment conducted by the Customer Experience (CX) team at Vanguard, a US-based investment management company. The experiment aimed to evaluate the impact of a new digital interface design on user experience and process completion rates.

### Introduction

In this project, we conducted an analysis of the digital experiment conducted by Vanguard's CX team. The experiment involved two groups: a control group that interacted with Vanguard's traditional online process and a test group that experienced the new, spruced-up digital interface. Our analysis focused on key performance indicators (KPIs) such as completion rate, average time spent on each step, and error rates to determine the effectiveness of the redesign.


### Data Description
The data includes information on the number of clients, completion rates, average time spent on each step, and error rates for both the control and test groups.

### Analysis Highlights

##### Completion Rate:
- Two-proportion, Two-sided Z-Test: This test aimed to determine if there was any difference in completion rates between the Test and Control groups. The null hypothesis (H0) stated that there is no difference, while the alternative hypothesis (HA) suggested that there is a difference. The calculated Z-statistic was 8.9 with an extremely low p-value (approximately 0), leading to the rejection of the null hypothesis. Thus, it was concluded that there is a significant difference in completion rates between the Test and Control groups.

- Two-proportion, One-sided Z-Test: This test aimed to determine if the completion rate for the Test group was significantly greater than 5% higher than the completion rate for the Control group. The null hypothesis (H0) stated that the completion rate difference was not significant, while the alternative hypothesis (HA) suggested that the completion rate for the Test group is significantly greater. The calculated Z-statistic was 2.70 with a p-value of 0.003, leading to the rejection of the null hypothesis. Therefore, it was concluded that the completion rate for the Test group is significantly greater than the completion rate for the Control group.

##### Average Time 
- Average Time per Step T-Tests:
For each process step, we conducted two-sided two-sample T-tests to determine if there was a significant difference in mean times between the test and control groups.
The null hypothesis (H0) stated that the difference in mean times between the test and control groups is zero, while the alternative hypothesis (HA) suggested that there is a difference.
The test statistics and p-values for each step indicated that we reject the null hypothesis for all steps, providing sufficient evidence to suggest a difference in mean times between the test and control groups.
- Total Process Time T-Test:
We conducted a two-sided two-sample T-test to compare the total process time between the test and control groups.
The null hypothesis (H0) stated that the difference in total process time between the test and control groups is zero, while the alternative hypothesis (HA) suggested that there is a difference.
The test statistic and p-value indicated that we reject the null hypothesis, providing sufficient evidence to suggest a difference in mean times between the test and control groups for the total process time.

##### Error rates:
- Error Rates for Each Process Step:
HO : Error Ratetest - Error Rate control ≥ 0
Null Hypothesis: There is no difference or the error rate in the test group is greater than or equal to the error rate in the contro group
HA: Error Ratetest - Error Rate control < 0
Alternative Hypothesis: The error rate in the test group is less than the error rate in the control group

Two-proportion one-sided Z-tests were conducted to compare error rates between the test and control groups for each process step.
For process steps 1 and 2, the high Z-scores and p-values close to 1 indicate that we fail to reject the null hypothesis, suggesting The test group exhibited more errors compared to the control group in these steps
However, for process steps 3 and confirm, the low p-values (< 0.05) and negative Z-scores indicate a statistically significant difference in error rates. The test group exhibited fewer errors compared to the control group in these steps.

HO : Error Ratetest - Error Rate contro =  0
HA: Error Ratetest - Error Rate control ≠ 0
Overall Error Rates for the Entire Process:
A two-proportion two-sided Z-test was conducted to compare the overall error rates between the test and control groups.
The high Z-statistic (20.14) and extremely low p-value (approximately 0) indicate a significant difference in error rates between the Test and Control groups for the entire process.

### Conclusion 

- The new digital design has successfully improved the user experience by enhancing completion rates. (69.29% to 65.58% &  Z-test p < 0.001)

- Users in the test group took less time (311 seconds) to complete the process compared to the control group (329 seconds), indicating a smoother and faster user journey.

- The test group had higher error rates in step 1 and 2 (most bacward navigation  step 1) suggesting areas for design improvement to reduce user errors.

Optimize Design: Address areas of higher error rates in the test group by optimizing design elements to enhance user clarity and reduce confusion.
Additional Data Needs: Incorporating direct feedback and qualitative data for deeper understanding of client responses.