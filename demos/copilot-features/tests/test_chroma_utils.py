"""Tests for Chroma utils."""
import pytest
from app.chroma_utils import chroma_slugify, chroma_generate_id, chroma_timestamp

def test_slugify():
    assert chroma_slugify("Hello World") == "hello-world"

def test_generate_id():
    id_ = chroma_generate_id()
    assert id_.startswith("chroma-")

def test_timestamp():
    ts = chroma_timestamp()
    assert ts.endswith("Z")
