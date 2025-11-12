#!/usr/bin/env python3
"""Test script for LaudoDataModel - Branch 1 testing"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from app.models import LaudoDataModel
from docx import Document

def print_section(title):
    """Print a section header."""
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def print_test(name, passed=True):
    """Print test result."""
    status = "✓ PASS" if passed else "✗ FAIL"
    print(f"{status}: {name}")

def main():
    print_section("Testing LaudoDataModel - Branch 1")
    
    # Test 1: Initialization
    print_section("Test 1: Model Initialization")
    try:
        model = LaudoDataModel()
        print_test("Model created successfully")
        print(f"  - Template path: {model.template_path}")
        print(f"  - Template loaded: {model.is_template_loaded()}")
        print(f"  - Patient data keys: {list(model.patient_data.keys())}")
        print(f"  - Resp1 data keys: {list(model.resp1_data.keys())}")
        print(f"  - Resp2 data keys: {list(model.resp2_data.keys())}")
        print(f"  - Psychologist data keys: {list(model.psychologist_data.keys())}")
    except Exception as e:
        print_test("Model created successfully", False)
        print(f"  ERROR: {e}")
        return
    
    # Test 2: Set Template
    print_section("Test 2: Set Template")
    try:
        test_doc = Document()
        model.set_template("/test/path/template.docx", test_doc)
        print_test("Template set successfully")
        print(f"  - Template path: {model.template_path}")
        print(f"  - Template loaded: {model.is_template_loaded()}")
        assert model.is_template_loaded(), "Template should be marked as loaded"
    except Exception as e:
        print_test("Template set successfully", False)
        print(f"  ERROR: {e}")
        return
    
    # Test 3: Set Patient Data
    print_section("Test 3: Set Patient Data")
    try:
        patient_data = {
            "patient_name": "João Silva",
            "patient_birth": "15/03/2010",
            "patient_crono_age": "14",
            "patient_school": "Escola Municipal",
            "patient_class": "8º Ano"
        }
        model.set_patient_data(patient_data)
        print_test("Patient data set successfully")
        for key, value in patient_data.items():
            print(f"  - {key}: {model.patient_data[key]} (expected: {value})")
            assert model.patient_data[key] == value, f"Patient data mismatch for {key}"
    except Exception as e:
        print_test("Patient data set successfully", False)
        print(f"  ERROR: {e}")
        return
    
    # Test 4: Set Respondent 1 Data
    print_section("Test 4: Set Respondent 1 Data")
    try:
        resp1_data = {
            "resp1_name": "Maria Silva",
            "resp1_career": "Professora",
            "resp1_education": "Superior Completo",
            "resp1_age": 35
        }
        model.set_resp1_data(resp1_data)
        print_test("Respondent 1 data set successfully")
        for key, value in resp1_data.items():
            print(f"  - {key}: {model.resp1_data[key]} (expected: {value})")
            assert model.resp1_data[key] == value, f"Resp1 data mismatch for {key}"
    except Exception as e:
        print_test("Respondent 1 data set successfully", False)
        print(f"  ERROR: {e}")
        return
    
    # Test 5: Set Respondent 2 Data
    print_section("Test 5: Set Respondent 2 Data")
    try:
        resp2_data = {
            "resp2_name": "José Silva",
            "resp2_career": "Engenheiro",
            "resp2_education": "Superior Completo",
            "resp2_age": 38
        }
        model.set_resp2_data(resp2_data)
        print_test("Respondent 2 data set successfully")
        for key, value in resp2_data.items():
            print(f"  - {key}: {model.resp2_data[key]} (expected: {value})")
            assert model.resp2_data[key] == value, f"Resp2 data mismatch for {key}"
    except Exception as e:
        print_test("Respondent 2 data set successfully", False)
        print(f"  ERROR: {e}")
        return
    
    # Test 6: Set Test Results
    print_section("Test 6: Set Test Results")
    try:
        test_results = {
            "QIT_out": "105",
            "ICV_out": "110",
            "IOP_out": "100"
        }
        model.set_test_results(test_results)
        print_test("Test results set successfully")
        for key, value in test_results.items():
            print(f"  - {key}: {model.test_results[key]} (expected: {value})")
            assert model.test_results[key] == value, f"Test result mismatch for {key}"
    except Exception as e:
        print_test("Test results set successfully", False)
        print(f"  ERROR: {e}")
        return
    
    # Test 7: Set Conclusion Text
    print_section("Test 7: Set Conclusion Text")
    try:
        conclusion = "Este é um texto de conclusão de teste para verificar o funcionamento do modelo de dados."
        model.set_conclusion_text(conclusion)
        print_test("Conclusion text set successfully")
        print(f"  - Conclusion: {model.conclusion_text}")
        assert model.conclusion_text == conclusion, "Conclusion text mismatch"
    except Exception as e:
        print_test("Conclusion text set successfully", False)
        print(f"  ERROR: {e}")
        return
    
    # Test 8: Set Psychologist Data
    print_section("Test 8: Set Psychologist Data")
    try:
        psychologist_data = {
            "nome_psicologo": "Dr. Ana Paula",
            "crp_psicologo": "CRP 06/123456"
        }
        model.set_psychologist_data(psychologist_data)
        print_test("Psychologist data set successfully")
        for key, value in psychologist_data.items():
            print(f"  - {key}: {model.psychologist_data[key]} (expected: {value})")
            assert model.psychologist_data[key] == value, f"Psychologist data mismatch for {key}"
    except Exception as e:
        print_test("Psychologist data set successfully", False)
        print(f"  ERROR: {e}")
        return
    
    # Test 9: Get All Data
    print_section("Test 9: Get All Data")
    try:
        all_data = model.get_all_data()
        print_test("Get all data successful")
        print(f"  - Keys in all_data: {list(all_data.keys())}")
        assert "template_path" in all_data
        assert "patient" in all_data
        assert "resp1" in all_data
        assert "resp2" in all_data
        assert "tests" in all_data
        assert "conclusion" in all_data
        assert "psychologist" in all_data
        print(f"  - Template path: {all_data['template_path']}")
        print(f"  - Patient name: {all_data['patient']['patient_name']}")
        print(f"  - Conclusion: {all_data['conclusion'][:50]}...")
    except Exception as e:
        print_test("Get all data successful", False)
        print(f"  ERROR: {e}")
        return
    
    # Test 10: Get Field Mapping
    print_section("Test 10: Get Field Mapping")
    try:
        field_mapping = model.get_field_mapping()
        print_test("Get field mapping successful")
        print(f"  - Total fields: {len(field_mapping)}")
        print(f"  - Sample fields:")
        sample_fields = list(field_mapping.items())[:10]
        for field, value in sample_fields:
            display_value = str(value)[:30] + "..." if len(str(value)) > 30 else str(value)
            print(f"    • {field}: {display_value}")
        
        # Verify some expected fields
        assert "patient_name" in field_mapping
        assert "resp1_name" in field_mapping
        assert "resp2_name" in field_mapping
        assert "conclusao_text" in field_mapping
        assert "nome_psicologo" in field_mapping
        assert field_mapping["patient_name"] == "João Silva"
    except Exception as e:
        print_test("Get field mapping successful", False)
        print(f"  ERROR: {e}")
        return
    
    # Test 11: To Dict Method
    print_section("Test 11: To Dict Method")
    try:
        dict_repr = model.to_dict()
        print_test("To dict method successful")
        print(f"  - Type: {type(dict_repr)}")
        print(f"  - Is dict: {isinstance(dict_repr, dict)}")
        assert isinstance(dict_repr, dict), "to_dict() should return a dict"
        assert dict_repr == model.get_all_data(), "to_dict() should match get_all_data()"
    except Exception as e:
        print_test("To dict method successful", False)
        print(f"  ERROR: {e}")
        return
    
    # Test 12: Partial Updates
    print_section("Test 12: Partial Data Updates")
    try:
        # Update only some patient fields
        model.set_patient_data({"patient_name": "João Silva Santos"})
        print_test("Partial update successful")
        print(f"  - Updated patient_name: {model.patient_data['patient_name']}")
        print(f"  - Other fields preserved: patient_birth = {model.patient_data['patient_birth']}")
        assert model.patient_data['patient_name'] == "João Silva Santos"
        assert model.patient_data['patient_birth'] == "15/03/2010"  # Should be preserved
    except Exception as e:
        print_test("Partial update successful", False)
        print(f"  ERROR: {e}")
        return
    
    # Final Summary
    print_section("Test Summary")
    print("✓ All tests passed successfully!")
    print("\nData Model Status:")
    print(f"  - Template loaded: {model.is_template_loaded()}")
    print(f"  - Patient data: {len([v for v in model.patient_data.values() if v])} fields filled")
    print(f"  - Respondent 1 data: {len([v for v in model.resp1_data.values() if v])} fields filled")
    print(f"  - Respondent 2 data: {len([v for v in model.resp2_data.values() if v])} fields filled")
    print(f"  - Test results: {len(model.test_results)} results")
    print(f"  - Conclusion: {'Set' if model.conclusion_text else 'Not set'}")
    print(f"  - Total field mappings: {len(model.get_field_mapping())}")

if __name__ == "__main__":
    main()

