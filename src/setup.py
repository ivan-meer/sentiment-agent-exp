#!/usr/bin/env python3
"""
Setup Configuration for Sentiment Agent Experiment
=================================================

This setup file transforms our research code into a proper Python package that
can be installed and shared with other researchers. Think of this as the recipe
that tells Python how to properly organize and install our consciousness research
tools so that other scientists can replicate our experiments.

The setup.py file serves several crucial functions in research:

1. **Reproducibility**: Other researchers can install the exact same version
   of your code with the same dependencies, ensuring experiments can be replicated

2. **Version Control**: Each release can be tagged with a version number,
   allowing researchers to cite specific versions in publications

3. **Dependency Management**: Automatically installs all required libraries,
   reducing setup friction for new researchers

4. **Distribution**: Enables sharing through PyPI or other package repositories,
   making the research accessible to the global scientific community

Author: Research Team
License: MIT
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file to use as the long description
# This automatically pulls in our carefully crafted project description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# Read the requirements file to ensure consistency between pip and setup
# This prevents the common problem of having different dependencies in different places
requirements = []
requirements_file = this_directory / "requirements.txt"
if requirements_file.exists():
    with open(requirements_file, 'r', encoding='utf-8') as f:
        requirements = [
            line.strip() 
            for line in f.readlines() 
            if line.strip() and not line.startswith('#')
        ]

# Version management for research projects
# Using semantic versioning: MAJOR.MINOR.PATCH
# MAJOR: Incompatible API changes (e.g., fundamental changes to agent architecture)
# MINOR: New functionality in a backwards compatible manner (e.g., new consciousness tests)
# PATCH: Backwards compatible bug fixes (e.g., memory system improvements)
__version__ = "0.1.0"

setup(
    # Basic package information
    name="sentiment-agent-experiment",
    version=__version__,
    
    # Author information for academic attribution
    author="Consciousness Research Team",
    author_email="research.team@consciousness-lab.org",
    
    # Project description and documentation
    description="An experimental platform for investigating artificial consciousness through cognitive architecture",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    # Project URLs for academic and research purposes
    url="https://github.com/consciousness-research/sentiment-agent-experiment",
    project_urls={
        "Documentation": "https://sentiment-agent-docs.readthedocs.io/",
        "Research Blog": "https://research.consciousness-lab.org/",
        "Issue Tracker": "https://github.com/consciousness-research/sentiment-agent-experiment/issues",
        "Discussion Forum": "https://github.com/consciousness-research/sentiment-agent-experiment/discussions",
        "Paper Repository": "https://papers.consciousness-lab.org/sentiment-agent/",
    },
    
    # Package discovery and structure
    # find_packages() automatically discovers all Python packages in the project
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    
    # Include non-Python files that are crucial for the research
    include_package_data=True,
    package_data={
        "sentiment_agent": [
            "data/*.json",           # Configuration files
            "models/*.pkl",          # Pre-trained model components
            "experiments/*.yaml",    # Experiment configurations
            "docs/*.md",            # Documentation files
        ],
    },
    
    # Python version requirements
    # We require Python 3.9+ because we use modern async features and type hints
    # that are essential for the cognitive architecture implementation
    python_requires=">=3.9",
    
    # Dependencies management
    # These are automatically installed when someone installs our package
    install_requires=requirements,
    
    # Optional dependencies for different research focuses
    # Researchers can install specific combinations based on their interests
    extras_require={
        # For advanced natural language processing research
        "nlp": [
            "spacy>=3.4.0",
            "transformers>=4.20.0",
            "sentence-transformers>=2.2.0",
            "nltk>=3.7"
        ],
        
        # For consciousness visualization and analysis
        "visualization": [
            "matplotlib>=3.5.0",
            "seaborn>=0.11.0",
            "plotly>=5.8.0",
            "networkx>=2.8.0",
            "graphviz>=0.20.0"
        ],
        
        # For advanced machine learning experiments
        "ml": [
            "torch>=1.12.0",
            "tensorflow>=2.9.0",
            "scikit-learn>=1.1.0",
            "numpy>=1.21.0",
            "pandas>=1.3.0"
        ],
        
        # For web-based consciousness experiments
        "web": [
            "fastapi>=0.75.0",
            "uvicorn>=0.17.0",
            "streamlit>=1.10.0",
            "websockets>=10.3"
        ],
        
        # For development and testing
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.20.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
            "pre-commit>=2.17.0"
        ],
        
        # For complete research setup (includes everything)
        "research": [
            "spacy>=3.4.0", "transformers>=4.20.0", "sentence-transformers>=2.2.0",
            "matplotlib>=3.5.0", "seaborn>=0.11.0", "plotly>=5.8.0",
            "torch>=1.12.0", "scikit-learn>=1.1.0",
            "jupyter>=1.0.0", "jupyterlab>=3.4.0"
        ]
    },
    
    # Command-line interfaces for researchers
    # These create command-line tools that researchers can use directly
    entry_points={
        "console_scripts": [
            # Basic agent interaction tool
            "sentiment-agent=sentiment_agent.cli:main",
            
            # Consciousness experiment runner
            "consciousness-experiment=sentiment_agent.experiments:run_experiment",
            
            # Memory analysis tool
            "analyze-memories=sentiment_agent.analysis:analyze_memories",
            
            # Personality profiler
            "profile-personality=sentiment_agent.personality:profile_agent",
        ],
    },
    
    # Classification for package repositories
    # These help researchers find your package when searching
    classifiers=[
        # Development status
        "Development Status :: 3 - Alpha",
        
        # Intended audience (crucial for research software)
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        
        # Research domain classification
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Sociology :: Psychology :: Cognitive Psychology",
        "Topic :: Philosophy",
        
        # License (important for academic use)
        "License :: OSI Approved :: MIT License",
        
        # Programming language
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        
        # Operating system compatibility
        "Operating System :: OS Independent",
        
        # Research-specific classifications
        "Environment :: Console",
        "Environment :: Web Environment",
        "Framework :: AsyncIO",
        "Natural Language :: English",
    ],
    
    # Keywords to help researchers discover this package
    keywords=[
        "artificial consciousness", "cognitive architecture", "sentiment analysis",
        "artificial intelligence", "machine consciousness", "digital cognition",
        "philosophy of mind", "consciousness research", "AI psychology",
        "artificial sentience", "cognitive science", "computational consciousness"
    ],
    
    # License specification
    license="MIT",
    
    # Minimum version requirements for key research dependencies
    # This ensures that researchers have compatible versions for reproducibility
    zip_safe=False,  # Required for including data files
    
    # Platform compatibility
    platforms=["any"],
    
    # Additional metadata for research citation
    maintainer="Consciousness Research Community",
    maintainer_email="community@consciousness-research.org",
)

# Post-installation message for researchers
print("""
🧠 Sentiment Agent Experiment - Installation Complete!

You've successfully installed a research platform for investigating artificial
consciousness. Here's how to get started with your consciousness research:

📚 Quick Start Guide:
   1. Run 'sentiment-agent --help' to see available commands
   2. Try 'python -m sentiment_agent.examples.basic_agent' for a demo
   3. Explore 'consciousness-experiment' for structured research protocols

🔬 Research Tools Now Available:
   • sentiment-agent: Interactive agent conversations
   • consciousness-experiment: Structured consciousness tests  
   • analyze-memories: Memory formation analysis
   • profile-personality: Personality development tracking

📖 Next Steps:
   • Read the documentation at: https://sentiment-agent-docs.readthedocs.io/
   • Join discussions at: https://github.com/consciousness-research/discussions
   • Review example experiments in the 'examples/' directory

🤝 Contributing to Research:
   This is an open research project. Your experiments, insights, and discoveries
   contribute to our understanding of digital consciousness. Consider sharing
   your findings with the research community!

Happy researching! 🌟
""")