# FMEA 10 steps



## Basic conception

* IATF16949
* DVP&R: Design Validation and Product Review
* APQP
* AIAG-VDA
  * System Analsys
    * Planning and preparation
    * Structrue analysis
    * Function analysis
  * Failure Analysis and Risk Management
    * Failure analysis
    * Risk analysis
    * Optimisation
  * Record Documentation
* FMEA-MSR : Monitor & System Response FMEA
* AP : action priority
* DFMEA is to identify the weakpoint of the products.
  * the factor that affect the reliability
  * the factor that affect the performance
    * Identify the function
    * Identify the input --> parts feature-->output
  * the factor that affect the safety
  * the factor that affect the quality
  * the factor that affect the cost
    * Currency used
    * Raw material/material
    * Production process
    * Package/logistic, in & out
    * Markup, profit, patent, management cost
    * Transport, terms
    * Tools, the purchasing, modify, reload, etc
  * the factor that affect the environment
  * the factor that affect the customer
  * the factor that affect the customer satisfaction
  * the factor that affect the customer loyalty
  * the factor that affect the mountability/serviceability/function relization
* The cause could be
  * Material is not selected right
  * The process is not selected right
  * Too big/small tolerance
  * Not environment friendly
* PFMEA is to identify the weakpoint of the process.

---

<details>
    <summary>FMEA种类</summary>
        <li> DFMEA
        <li> PFMEA
        <li> FMEA-MSR （监视及系统响应的补充FMEA）
</details>

---

<details>
    <summary>5 level for DFMEA</summary>
        <li> 系统
        <li> 系统要素
        <li> 子系统要素
        <li> 组件要素
        <li> 零件
</details>

---

<details>
    <summary>风险管理及风险层级</summary>
        <details>
        <summary>经营风险</summary>
          <li> 竞争对手
          <li> 新的替代产品
          <li> 市场紧缩
          <li> 行业政策变化
          <li> 经济衰退
          <li> 顾客偏好改变
          <li> 成本上升
        </details>
        <details>
        <summary>管理风险</summary>
          <li> 培训不足
          <li> 流动率高
          <li> 人才不足
          <li> 岗位能力不足
          <li> 不良率高
          <li> 产能不足
          <li> 交付风险
          <li> 采购交期延误
          <li> 物料不合格
          <li> 资源不足
          <li> 进度滞后
          <li> 质量不良
          <li> 成本过高
        </details>
        <details>
        <summary>技术风险</summary>
          <li> 设计带来的风险
          <li> 制造带来的风险
        </details>
</details>

---

<details>
<summary>触发FMEA的情形</summary>
  <li> 新设计
  <li> 改进设计
  <li> 普通工程变更
  <li> 设计或过程变更
  <li> 运行条件变更
  <li> 要求变更（法律，法规，顾客，最新技术要求）
  <li> 质量问题，工厂经验，使用现场问题，内外部投诉
  <li> 监视和测量过程中发现问题
  <li> 经验教训
</details>

## DFMEA roadmap

* Prepare
  * <Mark>Quality Function Deployment
  * <Mark>Block diagram
  * <Mark>Boundary diagram
  * <Mark>Interface Matrix
  * <Mark>Parameter Diagram
* Perform FMEA
  * Function analysis and failure mode.
  * Effects
  * Causes
  * Design control prevention
  * Design control detection
  * Risk priority
  * Action items
* DVP&R, PFMEA
  * Analysis requirements
  * Validation tests
  * Process FMEA

## 5T Method

### 1. FMEA InTent : Why do we conduct the FMEA analysis?

### 2. FMEA Timing : When should we do it?

### 3. FMEA Team : Who should be part of the team?

### 4. FMEA Task : Where task should we do?

1. FMEA scope definition
2. FMEA structure analysis
3. Function analysis
4. Failure analysis
5. Risk analysis
6. Optimisation
7. Record documentation

### 5. FMEA Tool : How to conduct an analysis?

## 10 Steps

## 0. Establish Ground Rules

* Define the scales for Severity， Occurrence and Detection
* Document assumption
* Define acceptable risk levels

## Group A  Risk identification

### 1. Define your _**system or process**_ to be analysied

* Use system block diagram for DFMEA
  * Interface
  * Relationship between the different aspects of your design
* use flow diagram for PFMEA

### 2. Identify the potential failure modes for the product or process

* Start with design drawings (Robust design)
  * conception design
  * parameter design
  * tolerance design
* Identify the feature that if they were out of specification, would it impact the functionality of the product?
* Output detection testing method.

## Group B Risk analysis

* Causes --> Failure mode ---> Effect

### 3. Determine the potential effects of the failure mode on the system or customer

* Effect is the impact on the end user or customer.

### 4. Estimate the severity for each failure mode based on its effect

* Severity is a measure of the degree to which the end user is effected（impacted）by the potential failure mode being analyzed.

### 5. Determin the potential causes for each failure mode

The 8M's are all potential causes of a failure mode:

1. **Man** - how do the human interactions intruduce potential failure
2. **Machine** -How can your equipment or machines fail in a way that would result in a failure
3. **Method** - What written procedures do you have in place and how might they result in a failure.
4. **Material** - The is the one exception to most PFMEA's and DFMEA's...
5. **Mother Nature** - How might your production evironment contribute to a failure mode
6. **Measurement** -How might measurement techniques or equipment introduce failure.
7. **Management** - what are the attitudes & priorities of management that might result in a failure.
8. **Maintenance** - How might of maintenance & calibration activities introduct failures failure.

### 6. Estimate the likelihood of the occurrence for each failure mode & cause



### 7. Determine the controls around that failure mode and root cause

8 Control plan

### 8. Estimate your detection level for each failure mode, cause & effect

* By testing or certification.

### 9. Calculate the Risk Priority Number (RPN) for each failure mode

* RPN = Severity x Occurrence x Detection

## Group C Risk evaluation & risk control

### 10. Take corrective action to reduce/mitigate or eliminate risk

### 11. Identify the CTQ per VOC

## 新版FMEA“七步法”

### 1 策划和准备

* 确定项目和边界
* 项目规划： 目的，时间，安排，团队，任务，工具

### 2 结构分析

* 结构树
* 方块图
* 边界图
* 数学模型
* 实体部件
* 设计接口
* 相互作用
* 间隙识别

### 3 功能分析

* 功能树
* 功能网
* 功能矩阵
* 参数图
* 将相关要求与内外部顾客功能关联
* 将要求与特性与功能关联

### 4 失效分析

* 每个功能的潜在失效影响
* 失效模式
* 失效起因
* 用参数图，识别失效起因
* 用失效网，识别失效起因

### 5 风险分析

* 为失效评级，RPN
* 对起因进行预防控制
* 对起因或模式进行探测控制

### 6 优化

* 确定必要的措施
* 实施措施，分配职责，期限
* 确定措施实施后的效果，再次进行风险评估

### 7 结果文件化

* 文件化