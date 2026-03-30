import os
import gspread
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def get_gspread_client():
    # 1. 스트림릿 서버 환경 (Secrets)
    if "gcp_service_account" in st.secrets:
        try:
            account = dict(st.secrets["gcp_service_account"])

            required_keys = [
                "type",
                "project_id",
                "private_key_id",
                "private_key",
                "client_email",
                "client_id",
                "auth_uri",
                "token_uri",
                "auth_provider_x509_cert_url",
                "client_x509_cert_url",
            ]

            missing = [k for k in required_keys if not account.get(k)]
            if missing:
                # 비밀 값 자체는 출력하지 않고 누락 키만 알려줌
                st.error(f"secrets 설정 누락: gcp_service_account의 {missing} 필드가 비어있습니다.")
                return None

            # Streamlit Cloud에서 private_key가 "\\n"으로 저장되는 경우 개행 정규화
            pk = account.get("private_key")
            if isinstance(pk, str) and ("\\n" in pk) and ("\n" not in pk):
                account["private_key"] = pk.replace("\\n", "\n")

            return gspread.service_account_from_dict(account)
        except Exception as e:
            st.error(f"gcp_service_account 인증 처리 실패: {e.__class__.__name__}: {e}")
            return None
    
    # 2. 로컬 환경 (.env 경로 기반)
    json_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if json_path and os.path.exists(json_path):
        return gspread.service_account(filename=json_path)
    
    return None

def get_sheet_id():
    sheet_id = st.secrets.get("GOOGLE_SHEET_ID") or os.getenv("GOOGLE_SHEET_ID")
    return str(sheet_id).strip() if sheet_id else sheet_id