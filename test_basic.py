#!/usr/bin/env python3
"""
Basic tests for the Video Editor Program.
These tests verify the structure and imports work correctly.
"""

import sys


def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")
    
    try:
        import video_editor
        print("✓ video_editor module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import video_editor: {e}")
        return False
    
    try:
        import cli
        print("✓ cli module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import cli: {e}")
        return False
    
    try:
        import examples
        print("✓ examples module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import examples: {e}")
        return False
    
    return True


def test_classes():
    """Test that main classes are available."""
    print("\nTesting classes...")
    
    try:
        from video_editor import VideoEditor, VideoMerger, create_title_video
        print("✓ VideoEditor class available")
        print("✓ VideoMerger class available")
        print("✓ create_title_video function available")
    except ImportError as e:
        print(f"✗ Failed to import classes: {e}")
        return False
    
    return True


def test_cli_help():
    """Test that CLI help works."""
    print("\nTesting CLI help...")
    
    import subprocess
    result = subprocess.run(
        [sys.executable, "cli.py", "--help"],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0 and "Video Editor Program" in result.stdout:
        print("✓ CLI help works")
        return True
    else:
        print(f"✗ CLI help failed")
        return False


def test_examples():
    """Test that examples can be run."""
    print("\nTesting examples...")
    
    try:
        import subprocess
        result = subprocess.run(
            [sys.executable, "examples.py"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if "Example Scripts" in result.stdout:
            print("✓ Examples script runs successfully")
            return True
        else:
            print("✗ Examples script output unexpected")
            return False
    except Exception as e:
        print(f"✗ Failed to run examples: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 70)
    print("Video Editor for InSoil - Basic Tests")
    print("=" * 70)
    
    results = []
    results.append(("Imports", test_imports()))
    results.append(("Classes", test_classes()))
    results.append(("CLI Help", test_cli_help()))
    results.append(("Examples", test_examples()))
    
    print("\n" + "=" * 70)
    print("Test Results:")
    print("=" * 70)
    
    all_passed = True
    for test_name, passed in results:
        status = "PASSED" if passed else "FAILED"
        print(f"{test_name}: {status}")
        if not passed:
            all_passed = False
    
    print("=" * 70)
    
    if all_passed:
        print("\n✓ All tests passed!")
        return 0
    else:
        print("\n✗ Some tests failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
