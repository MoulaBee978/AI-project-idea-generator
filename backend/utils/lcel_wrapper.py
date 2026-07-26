"""Lightweight LCEL wrapper with a safe fallback.

This module attempts to use LangChain's LCEL if available to evaluate
small expressions against project metadata (example: estimating time).
If LCEL is not available, it falls back to a deterministic Python mapper.
"""
from typing import Optional
import os

try:
    # LangChain's LCEL API location may vary between versions; try import
    from langchain.tools import LCEL  # type: ignore
    LCEL_AVAILABLE = True
except Exception:
    LCEL_AVAILABLE = False


def estimate_time_via_lcel(difficulty: str, tech_stack: str) -> str:
    """Estimate development time.

    Prefer LCEL when available; otherwise use a simple mapping.
    """
    difficulty = (difficulty or "").lower()
    tech = (tech_stack or "").lower()

    if LCEL_AVAILABLE:
        try:
            # Example expression - keep it simple and deterministic
            expr = (
                "if difficulty == 'beginner' then '1-2 weeks' "
                "elif difficulty == 'intermediate' then '3-6 weeks' "
                "elif difficulty == 'advanced' then '2-4 months' "
                "else '2-6 weeks'"
            )
            # The real LCEL usage would compile and run the expression; here we
            # show intent while remaining robust if the API shape differs.
            result = ""
            try:
                # If LCEL has a direct eval method, attempt it
                result = LCEL(expr).evaluate({"difficulty": difficulty, "tech": tech})  # type: ignore
            except Exception:
                result = None
            if result:
                return str(result)
        except Exception:
            pass

    # Fallback deterministic mapper
    if "beginner" in difficulty:
        return "1-2 weeks"
    if "intermediate" in difficulty:
        return "3-6 weeks"
    if "advanced" in difficulty:
        return "2-4 months"

    # Adjust for heavy stacks
    if any(s in tech for s in ("tensorflow", "spring", "django")):
        return "4-8 weeks"

    return "2-6 weeks"
