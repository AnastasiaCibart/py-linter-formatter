def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list[dict]) -> dict:
    return some_function(file_path, errors)


def some_function(file_path: str, errors: list[dict]) -> dict:
    errors = [error for error in errors if error.get("filename") == file_path]
    status = "passed"
    if errors:
        status = "failed"

    return {
        "errors": [
            {
                "line": error.get("line_number"),
                "column": error.get("column_number"),
                "message": error.get("text"),
                "name": error.get("code"),
                "source": "flake8"
            }
            for error in errors
        ],
        "path": file_path,
        "status": status
    }


def format_linter_report(linter_report: dict[str, list[dict]]) -> list[dict]:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in linter_report.items()
    ]
