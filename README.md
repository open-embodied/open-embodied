# Open-Embodied 

The Open Source Robot Real Time OS for the  Embodied  Time

embodied by

Harvard University, Stanford University, Peking University, BUPT and more


# open Embodied

# sim world DeepHunch

[DeepHunch](https://github.com/open-embodied/deephunch)

# Project Grand Plan

Unifying Robot Interfaces for the Era of Embodied Intelligence

# Development Studio

https://www.gitcc.com/dpqq-ros-agent/deep-ros-agent

# VLLM

https://www.gitcc.com

# Datasets

Opensource Embodied Datasets [Opensource Embodied Datasets](https://robot-ai.gitcc.com/)

# Book

The Open Landscape of Embodied AI[The Open Landscape of Embodied AI](https://aie.gitcc.com/aic/embodied/embodied-ai-en.html)




# The Ten Most Influential Open-Source Embodied AI Projects

> Data snapshot. Star counts are approximate at the time of writing and will keep moving; licences follow each repository's root `LICENSE`, and **model weights are often licensed differently from the code** — this is flagged separately in the table.


## 1. Master Table

| #  | Project                                      | GitHub                                                                                       | One-line positioning                                                     | Overview                                                                                                                                                                                                                                                                                                                           | Comparison and trade-offs                                                                                                                                                                                                                                                                                                                                                                    |
| -- | -------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | **LeRobot** (Hugging Face)                   | [huggingface/lerobot](https://github.com/huggingface/lerobot) · 28.4k★                       | The "transformers library" of embodied AI                                | A unified robot data format (LeRobotDataset), policy training scripts (ACT, Diffusion Policy, π₀, SmolVLA, GR00T adapters), and a complete real-robot deployment and teleoperation toolchain. Weights and datasets live on the Hugging Face Hub and load with a single `from_pretrained` call.                                     | **Lowest barrier to entry, broadest ecosystem** — the first repository a beginner should install. The cost is a thick abstraction layer: when something breaks you debug across two levels of source. Real-time low-level control is weak; high-frequency control loops must be built yourself. Good for "get it running fast and reproduce a baseline", not for low-level control research. |
| 2  | **openpi** (Physical Intelligence)           | [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) · 14.4k★     | Official open-source implementation of π₀ / π₀-FAST                      | The reference implementation of a flow-matching VLA, including inference and fine-tuning code for π₀, π₀-FAST and π₀.₅, a JAX training stack, and checkpoints for DROID and in-house robots. Designed around one model spanning many embodiments, pretrained on large multi-robot corpora.                                         | **Among the strongest open weights available**, with clearly better cross-embodiment generalisation than OpenVLA. The cost is JAX plus a bespoke training stack, so the engineering bar is high. π₀.6 and π₀.7 are not open source and are API-only, so a generation gap exists between the open and commercial versions. Suits teams with compute who intend to fine-tune and deploy.       |
| 3  | **Isaac GR00T** (NVIDIA)                     | [NVIDIA/Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T) · 8.3k★                          | Humanoid foundation model plus a simulation training ground              | GR00T N1.x is a dual-system VLA backbone (System 1 for fast reactions, System 2 for slow reasoning). It ships with [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) (8.4k★) for GPU-parallel simulation and synthetic data generation, closing the loop from simulated data to model training to real-robot deployment. | **The only open-source stack that truly connects simulation and model training**; the synthetic data pipeline is the core asset. **Licence trap: the code is Apache-2.0, but N1.6 weights are under a non-commercial NVIDIA licence; N1.7 onward moves to a commercial licence.** Suits humanoid and dual-arm teams with NVIDIA GPUs pursuing a simulation-first route.                      |
| 4  | **OpenVLA** (Stanford et al.)                | [openvla/openvla](https://github.com/openvla/openvla) · 7.2k★                                | The "paper-grade baseline" for open VLA                                  | A 7B model built on the Prismatic-7B vision-language model that discretises actions into tokens and decodes them autoregressively. Pretrained on 970k trajectories from OXE (Open X-Embodiment), with LoRA fine-tuning scripts; runs on a single A100.                                                                             | **The classic VLA baseline and the first choice for reproducing papers** — clean code, comparable results. The cost is slow autoregressive inference at 7B (roughly 6–10 Hz), accuracy lost to discretisation, and weaker generalisation than the π₀ family. Good for papers and teaching, not for high-frequency closed-loop control.                                                       |
| 5  | **Octo** (Berkeley et al.)                   | [octo-models/octo](https://github.com/octo-models/octo) · 1.6k★                              | Lightweight generalist robot policy (Transformer)                        | Two open generalist policies at 27M and 93M parameters, pretrained on OXE, supporting both language-instruction and goal-image conditioning across multiple embodiments, with complete examples for fine-tuning to new robots and tasks.                                                                                           | **Small, fast to infer, easy to fine-tune** — the value pick for "edge device plus a little data". The cost is a lower capability ceiling than large VLA models; complex long-horizon tasks strain it. Suits production pick-and-place work on robot arms.                                                                                                                                   |
| 6  | **Diffusion Policy** (Columbia / Stanford)   | [real-stanford/diffusion\_policy](https://github.com/real-stanford/diffusion_policy) · 4.3k★ | The original diffusion policy implementation                             | Models the multimodal distribution of action sequences with a diffusion model, solving the averaging problem where one scene admits several valid actions. Includes full experiment configs and pretrained weights for pusht, robomimic and real bimanual setups.                                                                  | **The methodological foundation — read it and run it.** It clearly beats MSE regression when actions are multimodal (for example, detouring around an obstacle). The cost is multi-step denoising at inference (10–20 steps) and high latency, plus no language conditioning. It is a **component, not a platform**, and is usually absorbed as an action head inside LeRobot or π₀.         |
| 7  | **Genesis** (Genesis-Embodied-AI)            | [Genesis-Embodied-AI/Genesis](https://github.com/Genesis-Embodied-AI/Genesis) · 30.2k★       | A generative physics engine built for embodied AI                        | A general-purpose physics engine written from scratch, built around extreme simulation speed (claimed to be an order of magnitude faster than Isaac Gym) and unified solving of rigid bodies, soft bodies, fluids and deformables, with a built-in generative data pipeline that can create scenes from natural language.          | **The highest star count in the field, with hype well ahead of maturity.** Speed and unified modelling are genuine strengths, but ecosystem, asset library and stability still trail the Isaac family; the claimed numbers need independent reproduction. Suits researchers generating data at scale; use with care in production.                                                           |
| 8  | **ManiSkill** (UCSD, Hao Su's group)         | [haosulab/ManiSkill](https://github.com/haosulab/ManiSkill) · 3.4k★                          | GPU-parallel manipulation simulation plus benchmarks                     | A SAPIEN-based manipulation simulator running tens of thousands of parallel environments on GPU, focused on dexterous manipulation with large demonstration datasets, offering RGBD, point-cloud and tactile observations across dozens of standard tasks.                                                                         | **The most practical simulator for manipulation**, balancing render quality against physical fidelity and producing data quickly. **Note: the code is permissive (Apache-2.0), but bundled assets such as YCB models are CC BY-NC — commercial use requires swapping them out.** Suits manipulation algorithm research and synthetic data.                                                   |
| 9  | **RoboCasa** (UT Austin / NVIDIA)            | [robocasa/robocasa](https://github.com/robocasa/robocasa) · 1.75k★                           | A large-scale benchmark for everyday kitchen tasks                       | Built on MuJoCo with 120+ kitchen scenes, 2,500+ objects and dozens of long-horizon household tasks (opening cabinets, loading a dishwasher, setting a table), plus human demonstrations and a generative asset creator.                                                                                                           | **The open benchmark closest to real household life** — long-horizon tasks and scene diversity are its signature. The cost is mediocre MuJoCo rendering, a larger sim-to-real gap, and a smaller community than ManiSkill. Suits long-horizon household tasks and imitation-learning evaluation.                                                                                             |
| 10 | **Habitat 3.0** (Meta / Georgia Tech et al.) | [facebookresearch/habitat-lab](https://github.com/facebookresearch/habitat-lab) · 3.2k★      | Indoor navigation and mobile manipulation with human-robot collaboration | A high-speed indoor simulator for embodied AI. Habitat 3.0 adds humanoid avatars and human-robot collaboration tasks (following a person while carrying something), with HM3D and HSSD scene datasets plus navigation and rearrangement benchmarks.                                                                                | **The de facto standard for navigation**, simulating at thousands of FPS per machine with scenes scanned from real homes. The limit is its focus on navigation and mobile manipulation; fine dexterous manipulation is weaker than in ManiSkill or RoboCasa. Suits SLAM, navigation and social robotics research.                                                                            |

## 2. Cross-Comparison: Scores by Dimension

Scored 1–5, where 5 is best. These reflect relative positioning, not absolute capability.

| Dimension                      | LeRobot | openpi | GR00T | OpenVLA | Octo | Diffusion Policy | Genesis | ManiSkill | RoboCasa | Habitat 3.0 |
| ------------------------------ | ------- | ------ | ----- | ------- | ---- | ---------------- | ------- | --------- | -------- | ----------- |
| Ease of adoption (5 = easiest) | 5       | 2      | 3     | 3       | 4    | 4                | 3       | 3         | 3        | 4           |
| Capability ceiling             | 4       | 5      | 5     | 3       | 2    | 2                | —       | —         | —        | —           |
| Ecosystem and docs             | 5       | 3      | 4     | 3       | 3    | 2                | 2       | 3         | 3        | 4           |
| Real-robot deployability       | 5       | 4      | 4     | 3       | 4    | 3                | 1       | 2         | 2        | 2           |
| Data / simulation output       | 2       | 2      | 5     | 1       | 1    | 3                | 5       | 5         | 4        | 4           |
| Licence friendliness           | 5       | 4      | 2     | 4       | 4    | 4                | 5       | 3         | 4        | 4           |
| Community activity (2026)      | 5       | 4      | 4     | 3       | 2    | 3                | 4       | 3         | 3        | 3           |

## 3. Grouped by Technical Route

| Route                                                   | Projects                                             | Verdict in one line                                                                                              |
| ------------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **End-to-end VLA (large model emits actions directly)** | openpi (π₀), GR00T N1.x, OpenVLA                     | Highest ceiling, highest compute cost. If you want generality, this is the only road.                            |
| **Lightweight generalist policies**                     | Octo, LeRobot's built-in SmolVLA / ACT               | Runs at the edge, trains on one GPU; good for fast vertical deployment.                                          |
| **Action-generation components**                        | Diffusion Policy (diffusion), π₀ (flow matching)     | Not a platform but an "action head" that handles multimodal action distributions and can be embedded in any VLA. |
| **Simulation and data infrastructure**                  | Isaac Lab, Genesis, ManiSkill, RoboCasa, Habitat 3.0 | Produces no policies; it produces **data and evaluation**. Without this layer, VLAs cannot be trained.           |

## 4. How to Choose: Four Paths for Four Situations

| Your situation                                                     | Recommended combination                                         | Why                                                                                                                                                         |
| ------------------------------------------------------------------ | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Complete beginner, wants a real robot running within two weeks** | LeRobot + SO-100/101 arm                                        | Cheap hardware (roughly ¥3–5k, about $420–700), complete tutorials, weights and datasets pulled straight from the Hub — a first grasping demo the same day. |
| **Writing papers, running controlled experiments**                 | OpenVLA or Octo as baseline + ManiSkill/RoboCasa for evaluation | Comparable baselines and accepted metrics; reviewers recognise this combination.                                                                            |
| **Has compute, wants to fine-tune for deployment**                 | openpi fine-tuning + Isaac Lab for data                         | π₀'s cross-embodiment generalisation substantially cuts the real-robot data you need; Isaac Lab fills the long tail of scenarios.                           |
| **Humanoids or long-horizon household tasks**                      | GR00T N1.x + RoboCasa evaluation                                | The dual-system architecture suits long-horizon work — but **confirm the weight licence first**; commercial use requires N1.7+.                             |

## 5. Three Facts You Must Know

1. **Open code ≠ open weights ≠ open data.** Of the ten, only LeRobot, OpenVLA, Octo and Diffusion Policy are essentially complete on all three. GR00T's weights are non-commercial, ManiSkill's assets are non-commercial, and π₀.6+ is not open source at all.
2. **Star count is not usability.** Genesis's 30.2k★ largely reflects launch-time virality; its engineering maturity is well below GR00T at 8.3k★. Octo has only 1.6k★ yet is the easiest of the ten to run on a real arm.
3. **Projects without a simulation layer do not scale.** Only five of the ten can genuinely generate their own data — GR00T (via Isaac Lab), Genesis, ManiSkill, RoboCasa and Habitat. Real-robot data costs roughly ¥10–100 per trajectory, which makes a pure real-robot strategy infeasible at scale.

---




# Core of The open embodied project

A Linux-like real-time operating system for Robotics

## Abstract

In the era of embodied intelligence, where robots are becoming increasingly integrated into our daily lives, the need for a unified robot interface has never been more pressing. Harvard University, Stanford University, Peking University, BUPT and other renowned institutions have jointly initiated the Open-Embodied project, aiming to create a comprehensive platform that encompasses robot operating systems, underlying control algorithms, and an application store for robot applications. This document outlines a grand plan for the Open-Embodied project, including its layered architecture, application-specific modules, and strategies for attracting global robotics researchers and manufacturers to participate.

## 1. Introduction

The Open-Embodied project is a response to the challenges posed by the proliferation of diverse robot systems and the lack of a standardized interface. By providing a unified platform, the project aims to facilitate the development, deployment, and management of robot applications, enabling seamless communication and interoperability between different robots and systems.

## 2. Layered Architecture

### 2.1 Hardware Abstraction Layer (HAL)

The Hardware Abstraction Layer serves as the interface between the robot hardware and the software components. It abstracts the hardware details, such as sensors, actuators, and communication interfaces, providing a standardized set of APIs for the upper layers. This allows developers to write software that is hardware-agnostic, making it easier to port applications across different robot platforms.

### 2.2 Operating System Layer (OSL)

The Operating System Layer provides a robust and flexible environment for running robot applications. It includes features such as task scheduling, memory management, and inter-process communication. The OSL will be based on a real-time operating system (RTOS) to ensure timely and reliable execution of critical tasks. It will also support multi-threading and multi-processing to take advantage of modern multi-core processors.

### 2.3 Middleware Layer (ML)

The Middleware Layer acts as a bridge between the OSL and the application layer. It provides a set of services and libraries for common robotics functionalities, such as localization, mapping, navigation, and manipulation. These services are implemented in a modular and reusable manner, allowing developers to easily integrate them into their applications. The ML will also support service discovery and composition, enabling dynamic and flexible application development.

### 2.4 Application Layer (AL)

The Application Layer is where robot applications are developed and deployed. It provides a user-friendly interface for developers to create, test, and manage their applications. The AL will include an application store, where developers can share and distribute their applications to a global audience. The application store will have features such as version control, user reviews, and ratings to ensure the quality and reliability of the applications.

## 3. Application-Specific Modules

### 3.1 Industrial Robotics Module

The Industrial Robotics Module focuses on the needs of industrial automation. It provides tools and libraries for tasks such as assembly, welding, painting, and material handling. The module will support integration with existing industrial control systems, such as PLCs (Programmable Logic Controllers), to enable seamless communication and coordination between robots and other equipment in the factory.

### 3.2 Service Robotics Module

The Service Robotics Module targets robots used in service industries, such as healthcare, hospitality, and logistics. It includes functionalities for tasks such as patient care, food delivery, and warehouse management. The module will emphasize human-robot interaction, providing natural language processing and gesture recognition capabilities to enable robots to understand and respond to human commands and gestures.

### 3.3 Agricultural Robotics Module

The Agricultural Robotics Module focuses on robots used in agriculture, such as autonomous tractors, drones for crop monitoring, and robotic harvesters. It provides tools and libraries for tasks such as planting, fertilizing, and harvesting crops. The module will take advantage of advanced sensors and imaging technologies to enable precise and efficient agricultural operations.

### 3.4 Educational Robotics Module

The Educational Robotics Module is designed for educational institutions and hobbyists. It provides a simple and intuitive interface for learning robotics programming and concepts. The module will include a set of pre-built robot models and simulation environments, allowing users to experiment with different robot configurations and scenarios without the need for physical hardware.

## 4. Strategies for Attracting Global Participation

### 4.1 Open Source Collaboration

The Open-Embodied project will be released as an open-source project, allowing researchers and manufacturers from around the world to contribute to its development. By providing a transparent and collaborative development environment, the project can benefit from the diverse expertise and perspectives of the global community. The project will use a version control system, such as Git, to manage the source code and track contributions from different developers.

### 4.2 Community Building

To foster a vibrant community around the Open-Embodied project, a series of community-building activities will be organized. These activities include online forums, workshops, and hackathons, where researchers and manufacturers can share their ideas, experiences, and best practices. The project will also establish a community governance model to ensure that the community's voice is heard and that the project's direction is aligned with the needs and interests of the community.

### 4.3 Partnerships and Alliances

The Open-Embodied project will seek partnerships and alliances with leading robotics companies, research institutions, and standards organizations. By collaborating with these partners, the project can gain access to resources, expertise, and market opportunities. For example, the project can partner with robotics companies to integrate their hardware and software solutions into the Open-Embodied platform, or with research institutions to conduct joint research projects on advanced robotics technologies.

### 4.4 Education and Training

To ensure that researchers and manufacturers have the necessary skills and knowledge to participate in the Open-Embodied project, a comprehensive education and training program will be developed. This program will include online courses, tutorials, and workshops on robotics programming, system integration, and application development. The project will also provide documentation and support materials to help users get started and troubleshoot issues.

### 4.5 Recognition and Rewards

To incentivize participation in the Open-Embodied project, a recognition and rewards system will be established. This system will recognize and reward developers who make significant contributions to the project, such as developing new features, fixing bugs, or creating high-quality applications. Rewards can include public recognition, prizes, and opportunities to collaborate with leading robotics companies and research institutions.

## 5. Technical Architecture

### 5.1 Communication Protocols

The Open-Embodied project will adopt standardized communication protocols to ensure seamless communication between different layers and modules. These protocols will be based on industry standards, such as ROS (Robot Operating System) communication protocols, to ensure compatibility with existing robotics systems. The project will also support custom communication protocols for specific application scenarios, allowing developers to optimize communication performance for their needs.

### 5.2 Data Management

Effective data management is crucial for the Open-Embodied project, as robots generate large amounts of data during operation. The project will implement a centralized data management system that can store, process, and analyze robot data in real-time. This system will support data sharing and collaboration between different applications and users, enabling researchers and manufacturers to leverage each other's data for better decision-making and innovation.

### 5.3 Security and Privacy

Security and privacy are important considerations for the Open-Embodied project, especially when dealing with sensitive data and communication between robots and external systems. The project will implement robust security measures, such as encryption, authentication, and access control, to protect against unauthorized access and data breaches. It will also comply with relevant privacy regulations, ensuring that user data is handled in a secure and compliant manner.

## 6. Conclusion

The Open-Embodied project is a grand initiative aimed at unifying robot interfaces for the era of embodied intelligence. By adopting a layered architecture, application-specific modules, and a series of strategies for attracting global participation, the project can create a vibrant and collaborative ecosystem that drives innovation and advancement in the field of robotics. The project's open-source nature, community-building activities, and education and training programs will ensure that researchers and manufacturers from around the world can contribute to and benefit from the project. With the support of leading robotics companies, research institutions, and standards organizations, the Open-Embodied project has the potential to become the de facto standard for robot interfaces, enabling seamless communication and interoperability between different robot platforms and systems.


## Acknowledgements

open-embodied has benefitted from the following projects/resources.

--RROS
  [BUPT RROS](https://github.com/BUPT-OS/RROS)

- [Evl/xenomai (linux-evl)](https://evlproject.org/core/). We learned from evl core how to implement a dual kernel and use dovetail for interrupt virtualization and libevl for user library. Thanks, @Philippe for his genius work and patient explanation in the riot!
- [Rust-for-Linux](https://github.com/Rust-for-Linux/linux): We use RFL to write RROS in Linux. We ask a lot of questions on RFL Zulip and constructing safety abstractions. Kudos to @ojeda, @Wedson,  @Alex, @boqun, @Gary, @Björn in the RFL community for patiently helping us. We hope to bring more safety abstraction back to the RFL in return!
- [Muduo](https://www.cnblogs.com/wsg1100/p/13836497.html): His detailed blog gives us insights for xenomai/evl project.
- All prospective contributors to RROS in the future!



# Project Grand Plan

Unifying Robot Interfaces for the Era of Embodied Intelligence

# Development Studio

https://www.gitcc.com/dpqq-ros-agent/deep-ros-agent

# VLLM

https://www.gitcc.com

# Datasets

Opensource Embodied Datasets [Opensource Embodied Datasets](https://robot-ai.gitcc.com/)

# Book

The Open Landscape of Embodied AI[The Open Landscape of Embodied AI](https://aie.gitcc.com/aic/embodied/embodied-ai-en.html)




# How TO Get Data

data [data](https://aie.gitcc.com/aic/talk/embodied-data-2026.html)

# Benchmark

[Benchmark](https://aie.gitcc.com/aic/talk/embodied-benchmark-book.html)

# Top Open source Projects

# Data, Benchmark and List

by DeepOpen  数据、基准和榜单 [数据、基准和榜单](https://aie.gitcc.com/aic/talk/embodied-data-2026.html)

by DeepOpen  Data, Benchmark and List [Data, Benchmark and List](https://aie.gitcc.com/aic/talk/embodied-data-2026.html)

supported by DeepOpen  www.deepopen.com

study roadmap:  https://github.com/deepopen-com/deepopen-talks-awesome
[study readmap](https://github.com/deepopen-com/deepopen-talks-awesome)
