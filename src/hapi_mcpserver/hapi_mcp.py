# MCP tool stubs for all FHIR resources with descriptions
from fastmcp import FastMCP
import requests
from typing import Dict, Any

FHIR_BASE = "http://localhost:8080/fhir"
mcp = FastMCP('My MCP Server')

@mcp.tool
def create_account(data: dict) -> Dict[str, Any]:
    """Create a Account. The Account FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Account"""
    resp = requests.post(f'{FHIR_BASE}/Account', json=data)
    return resp.json()

@mcp.tool
def get_account(resource_id: str) -> Dict[str, Any]:
    """Get a Account by ID. The Account FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Account"""
    resp = requests.get(f'{FHIR_BASE}/Account/{resource_id}')
    return resp.json()

@mcp.tool
def search_account(params: dict) -> Dict[str, Any]:
    """Search Account resources. The Account FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Account"""
    resp = requests.get(f'{FHIR_BASE}/Account', params=params)
    return resp.json()

@mcp.tool
def create_activitydefinition(data: dict) -> Dict[str, Any]:
    """Create a ActivityDefinition. The ActivityDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ActivityDefinition<br/>Supported profile: http://hl7.org.nz/fhir/StructureDefinition/CcaActivityDefinition"""
    resp = requests.post(f'{FHIR_BASE}/ActivityDefinition', json=data)
    return resp.json()

@mcp.tool
def get_activitydefinition(resource_id: str) -> Dict[str, Any]:
    """Get a ActivityDefinition by ID. The ActivityDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ActivityDefinition<br/>Supported profile: http://hl7.org.nz/fhir/StructureDefinition/CcaActivityDefinition"""
    resp = requests.get(f'{FHIR_BASE}/ActivityDefinition/{resource_id}')
    return resp.json()

@mcp.tool
def search_activitydefinition(params: dict) -> Dict[str, Any]:
    """Search ActivityDefinition resources. The ActivityDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ActivityDefinition<br/>Supported profile: http://hl7.org.nz/fhir/StructureDefinition/CcaActivityDefinition"""
    resp = requests.get(f'{FHIR_BASE}/ActivityDefinition', params=params)
    return resp.json()

@mcp.tool
def create_adverseevent(data: dict) -> Dict[str, Any]:
    """Create a AdverseEvent. The AdverseEvent FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/AdverseEvent"""
    resp = requests.post(f'{FHIR_BASE}/AdverseEvent', json=data)
    return resp.json()

@mcp.tool
def get_adverseevent(resource_id: str) -> Dict[str, Any]:
    """Get a AdverseEvent by ID. The AdverseEvent FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/AdverseEvent"""
    resp = requests.get(f'{FHIR_BASE}/AdverseEvent/{resource_id}')
    return resp.json()

@mcp.tool
def search_adverseevent(params: dict) -> Dict[str, Any]:
    """Search AdverseEvent resources. The AdverseEvent FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/AdverseEvent"""
    resp = requests.get(f'{FHIR_BASE}/AdverseEvent', params=params)
    return resp.json()

@mcp.tool
def create_allergyintolerance(data: dict) -> Dict[str, Any]:
    """Create a AllergyIntolerance. The AllergyIntolerance FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/AllergyIntolerance<br/>Supported profile: http://example.org/fhir/StructureDefinition/CRSAllergyIntolerance<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-allergyintolerance<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-allergyintolerance-S123<br/>Supported profile: https://www.ehealth.fgov.be/standards/fhir/StructureDefinition/be-allergyintolerance"""
    resp = requests.post(f'{FHIR_BASE}/AllergyIntolerance', json=data)
    return resp.json()

@mcp.tool
def get_allergyintolerance(resource_id: str) -> Dict[str, Any]:
    """Get a AllergyIntolerance by ID. The AllergyIntolerance FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/AllergyIntolerance<br/>Supported profile: http://example.org/fhir/StructureDefinition/CRSAllergyIntolerance<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-allergyintolerance<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-allergyintolerance-S123<br/>Supported profile: https://www.ehealth.fgov.be/standards/fhir/StructureDefinition/be-allergyintolerance"""
    resp = requests.get(f'{FHIR_BASE}/AllergyIntolerance/{resource_id}')
    return resp.json()

@mcp.tool
def search_allergyintolerance(params: dict) -> Dict[str, Any]:
    """Search AllergyIntolerance resources. The AllergyIntolerance FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/AllergyIntolerance<br/>Supported profile: http://example.org/fhir/StructureDefinition/CRSAllergyIntolerance<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-allergyintolerance<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-allergyintolerance-S123<br/>Supported profile: https://www.ehealth.fgov.be/standards/fhir/StructureDefinition/be-allergyintolerance"""
    resp = requests.get(f'{FHIR_BASE}/AllergyIntolerance', params=params)
    return resp.json()

@mcp.tool
def create_appointment(data: dict) -> Dict[str, Any]:
    """Create a Appointment. The Appointment FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Appointment<br/>Supported profile: http://ehealthontario.on.ca/fhir/StructureDefinition/eReferral-appointment"""
    resp = requests.post(f'{FHIR_BASE}/Appointment', json=data)
    return resp.json()

@mcp.tool
def get_appointment(resource_id: str) -> Dict[str, Any]:
    """Get a Appointment by ID. The Appointment FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Appointment<br/>Supported profile: http://ehealthontario.on.ca/fhir/StructureDefinition/eReferral-appointment"""
    resp = requests.get(f'{FHIR_BASE}/Appointment/{resource_id}')
    return resp.json()

@mcp.tool
def search_appointment(params: dict) -> Dict[str, Any]:
    """Search Appointment resources. The Appointment FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Appointment<br/>Supported profile: http://ehealthontario.on.ca/fhir/StructureDefinition/eReferral-appointment"""
    resp = requests.get(f'{FHIR_BASE}/Appointment', params=params)
    return resp.json()

@mcp.tool
def create_appointmentresponse(data: dict) -> Dict[str, Any]:
    """Create a AppointmentResponse. The AppointmentResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/AppointmentResponse"""
    resp = requests.post(f'{FHIR_BASE}/AppointmentResponse', json=data)
    return resp.json()

@mcp.tool
def get_appointmentresponse(resource_id: str) -> Dict[str, Any]:
    """Get a AppointmentResponse by ID. The AppointmentResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/AppointmentResponse"""
    resp = requests.get(f'{FHIR_BASE}/AppointmentResponse/{resource_id}')
    return resp.json()

@mcp.tool
def search_appointmentresponse(params: dict) -> Dict[str, Any]:
    """Search AppointmentResponse resources. The AppointmentResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/AppointmentResponse"""
    resp = requests.get(f'{FHIR_BASE}/AppointmentResponse', params=params)
    return resp.json()

@mcp.tool
def create_auditevent(data: dict) -> Dict[str, Any]:
    """Create a AuditEvent. The AuditEvent FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/AuditEvent<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventBase<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventCreate<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventDelete<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventRead<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventSearch<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventUpdate<br/>Supported profile: http://test.com/fhir/structuredefinition/test-parent"""
    resp = requests.post(f'{FHIR_BASE}/AuditEvent', json=data)
    return resp.json()

@mcp.tool
def get_auditevent(resource_id: str) -> Dict[str, Any]:
    """Get a AuditEvent by ID. The AuditEvent FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/AuditEvent<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventBase<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventCreate<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventDelete<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventRead<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventSearch<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventUpdate<br/>Supported profile: http://test.com/fhir/structuredefinition/test-parent"""
    resp = requests.get(f'{FHIR_BASE}/AuditEvent/{resource_id}')
    return resp.json()

@mcp.tool
def search_auditevent(params: dict) -> Dict[str, Any]:
    """Search AuditEvent resources. The AuditEvent FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/AuditEvent<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventBase<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventCreate<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventDelete<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventRead<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventSearch<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/AuditEventUpdate<br/>Supported profile: http://test.com/fhir/structuredefinition/test-parent"""
    resp = requests.get(f'{FHIR_BASE}/AuditEvent', params=params)
    return resp.json()

@mcp.tool
def create_basic(data: dict) -> Dict[str, Any]:
    """Create a Basic. The Basic FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Basic<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/SVC-Basic-QRCode"""
    resp = requests.post(f'{FHIR_BASE}/Basic', json=data)
    return resp.json()

@mcp.tool
def get_basic(resource_id: str) -> Dict[str, Any]:
    """Get a Basic by ID. The Basic FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Basic<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/SVC-Basic-QRCode"""
    resp = requests.get(f'{FHIR_BASE}/Basic/{resource_id}')
    return resp.json()

@mcp.tool
def search_basic(params: dict) -> Dict[str, Any]:
    """Search Basic resources. The Basic FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Basic<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/SVC-Basic-QRCode"""
    resp = requests.get(f'{FHIR_BASE}/Basic', params=params)
    return resp.json()

@mcp.tool
def create_binary(data: dict) -> Dict[str, Any]:
    """Create a Binary. The Binary FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Binary<br/>Supported profile: http://fhir.gevko.de/fhir/StructureDefinition/EVoBinary<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/DDCCBinaryQR<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/DDCCBinaryQRContent<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/DDCCBinaryQRPNG<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-binary-qr<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-binary-qrcontent<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-binary-qrpng"""
    resp = requests.post(f'{FHIR_BASE}/Binary', json=data)
    return resp.json()

@mcp.tool
def get_binary(resource_id: str) -> Dict[str, Any]:
    """Get a Binary by ID. The Binary FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Binary<br/>Supported profile: http://fhir.gevko.de/fhir/StructureDefinition/EVoBinary<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/DDCCBinaryQR<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/DDCCBinaryQRContent<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/DDCCBinaryQRPNG<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-binary-qr<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-binary-qrcontent<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-binary-qrpng"""
    resp = requests.get(f'{FHIR_BASE}/Binary/{resource_id}')
    return resp.json()

@mcp.tool
def search_binary(params: dict) -> Dict[str, Any]:
    """Search Binary resources. The Binary FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Binary<br/>Supported profile: http://fhir.gevko.de/fhir/StructureDefinition/EVoBinary<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/DDCCBinaryQR<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/DDCCBinaryQRContent<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/DDCCBinaryQRPNG<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-binary-qr<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-binary-qrcontent<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-binary-qrpng"""
    resp = requests.get(f'{FHIR_BASE}/Binary', params=params)
    return resp.json()

@mcp.tool
def create_biologicallyderivedproduct(data: dict) -> Dict[str, Any]:
    """Create a BiologicallyDerivedProduct. The BiologicallyDerivedProduct FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct"""
    resp = requests.post(f'{FHIR_BASE}/BiologicallyDerivedProduct', json=data)
    return resp.json()

@mcp.tool
def get_biologicallyderivedproduct(resource_id: str) -> Dict[str, Any]:
    """Get a BiologicallyDerivedProduct by ID. The BiologicallyDerivedProduct FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct"""
    resp = requests.get(f'{FHIR_BASE}/BiologicallyDerivedProduct/{resource_id}')
    return resp.json()

@mcp.tool
def search_biologicallyderivedproduct(params: dict) -> Dict[str, Any]:
    """Search BiologicallyDerivedProduct resources. The BiologicallyDerivedProduct FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct"""
    resp = requests.get(f'{FHIR_BASE}/BiologicallyDerivedProduct', params=params)
    return resp.json()

@mcp.tool
def create_bodystructure(data: dict) -> Dict[str, Any]:
    """Create a BodyStructure. The BodyStructure FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/BodyStructure"""
    resp = requests.post(f'{FHIR_BASE}/BodyStructure', json=data)
    return resp.json()

@mcp.tool
def get_bodystructure(resource_id: str) -> Dict[str, Any]:
    """Get a BodyStructure by ID. The BodyStructure FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/BodyStructure"""
    resp = requests.get(f'{FHIR_BASE}/BodyStructure/{resource_id}')
    return resp.json()

@mcp.tool
def search_bodystructure(params: dict) -> Dict[str, Any]:
    """Search BodyStructure resources. The BodyStructure FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/BodyStructure"""
    resp = requests.get(f'{FHIR_BASE}/BodyStructure', params=params)
    return resp.json()

@mcp.tool
def create_bundle(data: dict) -> Dict[str, Any]:
    """Create a Bundle. The Bundle FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Bundle<br/>Supported profile: http://fhir.gevko.de/fhir/StructureDefinition/EVoBundle<br/>Supported profile: http://fkcfhir.org/fhir/StructureDefinition/RequestBundle<br/>Supported profile: http://hl7.eu/fhir/ig/dgc/StructureDefinition/Bundle-dgc<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/library-bundle-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/measure-bundle-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/testcase-bundle-cqfm<br/>Supported profile: http://hl7.org/fhir/us/dme-orders/StructureDefinition/PAO-bundle4<br/>Supported profile: http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-subscription-notification<br/>Supported profile: http://trilliumbridge.eu/fhir/StructureDefinition/bundle-ips-uv-trillium2<br/>Supported profile: https://ghit42796.github.io/fhir_test/StructureDefinition-Vaccine-Certificate-Bundle<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/DDCCBundle<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-bundle<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-submit-health-event-request<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-submit-health-event-response"""
    resp = requests.post(f'{FHIR_BASE}/Bundle', json=data)
    return resp.json()

@mcp.tool
def get_bundle(resource_id: str) -> Dict[str, Any]:
    """Get a Bundle by ID. The Bundle FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Bundle<br/>Supported profile: http://fhir.gevko.de/fhir/StructureDefinition/EVoBundle<br/>Supported profile: http://fkcfhir.org/fhir/StructureDefinition/RequestBundle<br/>Supported profile: http://hl7.eu/fhir/ig/dgc/StructureDefinition/Bundle-dgc<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/library-bundle-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/measure-bundle-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/testcase-bundle-cqfm<br/>Supported profile: http://hl7.org/fhir/us/dme-orders/StructureDefinition/PAO-bundle4<br/>Supported profile: http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-subscription-notification<br/>Supported profile: http://trilliumbridge.eu/fhir/StructureDefinition/bundle-ips-uv-trillium2<br/>Supported profile: https://ghit42796.github.io/fhir_test/StructureDefinition-Vaccine-Certificate-Bundle<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/DDCCBundle<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-bundle<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-submit-health-event-request<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-submit-health-event-response"""
    resp = requests.get(f'{FHIR_BASE}/Bundle/{resource_id}')
    return resp.json()

@mcp.tool
def search_bundle(params: dict) -> Dict[str, Any]:
    """Search Bundle resources. The Bundle FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Bundle<br/>Supported profile: http://fhir.gevko.de/fhir/StructureDefinition/EVoBundle<br/>Supported profile: http://fkcfhir.org/fhir/StructureDefinition/RequestBundle<br/>Supported profile: http://hl7.eu/fhir/ig/dgc/StructureDefinition/Bundle-dgc<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/library-bundle-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/measure-bundle-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/testcase-bundle-cqfm<br/>Supported profile: http://hl7.org/fhir/us/dme-orders/StructureDefinition/PAO-bundle4<br/>Supported profile: http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-subscription-notification<br/>Supported profile: http://trilliumbridge.eu/fhir/StructureDefinition/bundle-ips-uv-trillium2<br/>Supported profile: https://ghit42796.github.io/fhir_test/StructureDefinition-Vaccine-Certificate-Bundle<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/DDCCBundle<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-bundle<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-submit-health-event-request<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-submit-health-event-response"""
    resp = requests.get(f'{FHIR_BASE}/Bundle', params=params)
    return resp.json()

@mcp.tool
def create_capabilitystatement(data: dict) -> Dict[str, Any]:
    """Create a CapabilityStatement. The CapabilityStatement FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CapabilityStatement<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/CapabilityStatementWithSlices"""
    resp = requests.post(f'{FHIR_BASE}/CapabilityStatement', json=data)
    return resp.json()

@mcp.tool
def get_capabilitystatement(resource_id: str) -> Dict[str, Any]:
    """Get a CapabilityStatement by ID. The CapabilityStatement FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CapabilityStatement<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/CapabilityStatementWithSlices"""
    resp = requests.get(f'{FHIR_BASE}/CapabilityStatement/{resource_id}')
    return resp.json()

@mcp.tool
def search_capabilitystatement(params: dict) -> Dict[str, Any]:
    """Search CapabilityStatement resources. The CapabilityStatement FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CapabilityStatement<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/CapabilityStatementWithSlices"""
    resp = requests.get(f'{FHIR_BASE}/CapabilityStatement', params=params)
    return resp.json()

@mcp.tool
def create_careplan(data: dict) -> Dict[str, Any]:
    """Create a CarePlan. The CarePlan FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CarePlan<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-careplan"""
    resp = requests.post(f'{FHIR_BASE}/CarePlan', json=data)
    return resp.json()

@mcp.tool
def get_careplan(resource_id: str) -> Dict[str, Any]:
    """Get a CarePlan by ID. The CarePlan FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CarePlan<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-careplan"""
    resp = requests.get(f'{FHIR_BASE}/CarePlan/{resource_id}')
    return resp.json()

@mcp.tool
def search_careplan(params: dict) -> Dict[str, Any]:
    """Search CarePlan resources. The CarePlan FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CarePlan<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-careplan"""
    resp = requests.get(f'{FHIR_BASE}/CarePlan', params=params)
    return resp.json()

@mcp.tool
def create_careteam(data: dict) -> Dict[str, Any]:
    """Create a CareTeam. The CareTeam FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CareTeam<br/>Supported profile: http://example.org/fhir/StructureDefinition/MyCareTeam<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-careteam"""
    resp = requests.post(f'{FHIR_BASE}/CareTeam', json=data)
    return resp.json()

@mcp.tool
def get_careteam(resource_id: str) -> Dict[str, Any]:
    """Get a CareTeam by ID. The CareTeam FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CareTeam<br/>Supported profile: http://example.org/fhir/StructureDefinition/MyCareTeam<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-careteam"""
    resp = requests.get(f'{FHIR_BASE}/CareTeam/{resource_id}')
    return resp.json()

@mcp.tool
def search_careteam(params: dict) -> Dict[str, Any]:
    """Search CareTeam resources. The CareTeam FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CareTeam<br/>Supported profile: http://example.org/fhir/StructureDefinition/MyCareTeam<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-careteam"""
    resp = requests.get(f'{FHIR_BASE}/CareTeam', params=params)
    return resp.json()

@mcp.tool
def create_catalogentry(data: dict) -> Dict[str, Any]:
    """Create a CatalogEntry. The CatalogEntry FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CatalogEntry"""
    resp = requests.post(f'{FHIR_BASE}/CatalogEntry', json=data)
    return resp.json()

@mcp.tool
def get_catalogentry(resource_id: str) -> Dict[str, Any]:
    """Get a CatalogEntry by ID. The CatalogEntry FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CatalogEntry"""
    resp = requests.get(f'{FHIR_BASE}/CatalogEntry/{resource_id}')
    return resp.json()

@mcp.tool
def search_catalogentry(params: dict) -> Dict[str, Any]:
    """Search CatalogEntry resources. The CatalogEntry FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CatalogEntry"""
    resp = requests.get(f'{FHIR_BASE}/CatalogEntry', params=params)
    return resp.json()

@mcp.tool
def create_chargeitem(data: dict) -> Dict[str, Any]:
    """Create a ChargeItem. The ChargeItem FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ChargeItem"""
    resp = requests.post(f'{FHIR_BASE}/ChargeItem', json=data)
    return resp.json()

@mcp.tool
def get_chargeitem(resource_id: str) -> Dict[str, Any]:
    """Get a ChargeItem by ID. The ChargeItem FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ChargeItem"""
    resp = requests.get(f'{FHIR_BASE}/ChargeItem/{resource_id}')
    return resp.json()

@mcp.tool
def search_chargeitem(params: dict) -> Dict[str, Any]:
    """Search ChargeItem resources. The ChargeItem FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ChargeItem"""
    resp = requests.get(f'{FHIR_BASE}/ChargeItem', params=params)
    return resp.json()

@mcp.tool
def create_chargeitemdefinition(data: dict) -> Dict[str, Any]:
    """Create a ChargeItemDefinition. The ChargeItemDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ChargeItemDefinition"""
    resp = requests.post(f'{FHIR_BASE}/ChargeItemDefinition', json=data)
    return resp.json()

@mcp.tool
def get_chargeitemdefinition(resource_id: str) -> Dict[str, Any]:
    """Get a ChargeItemDefinition by ID. The ChargeItemDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ChargeItemDefinition"""
    resp = requests.get(f'{FHIR_BASE}/ChargeItemDefinition/{resource_id}')
    return resp.json()

@mcp.tool
def search_chargeitemdefinition(params: dict) -> Dict[str, Any]:
    """Search ChargeItemDefinition resources. The ChargeItemDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ChargeItemDefinition"""
    resp = requests.get(f'{FHIR_BASE}/ChargeItemDefinition', params=params)
    return resp.json()

@mcp.tool
def create_claim(data: dict) -> Dict[str, Any]:
    """Create a Claim. The Claim FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Claim"""
    resp = requests.post(f'{FHIR_BASE}/Claim', json=data)
    return resp.json()

@mcp.tool
def get_claim(resource_id: str) -> Dict[str, Any]:
    """Get a Claim by ID. The Claim FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Claim"""
    resp = requests.get(f'{FHIR_BASE}/Claim/{resource_id}')
    return resp.json()

@mcp.tool
def search_claim(params: dict) -> Dict[str, Any]:
    """Search Claim resources. The Claim FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Claim"""
    resp = requests.get(f'{FHIR_BASE}/Claim', params=params)
    return resp.json()

@mcp.tool
def create_claimresponse(data: dict) -> Dict[str, Any]:
    """Create a ClaimResponse. The ClaimResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ClaimResponse"""
    resp = requests.post(f'{FHIR_BASE}/ClaimResponse', json=data)
    return resp.json()

@mcp.tool
def get_claimresponse(resource_id: str) -> Dict[str, Any]:
    """Get a ClaimResponse by ID. The ClaimResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ClaimResponse"""
    resp = requests.get(f'{FHIR_BASE}/ClaimResponse/{resource_id}')
    return resp.json()

@mcp.tool
def search_claimresponse(params: dict) -> Dict[str, Any]:
    """Search ClaimResponse resources. The ClaimResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ClaimResponse"""
    resp = requests.get(f'{FHIR_BASE}/ClaimResponse', params=params)
    return resp.json()

@mcp.tool
def create_clinicalimpression(data: dict) -> Dict[str, Any]:
    """Create a ClinicalImpression. The ClinicalImpression FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ClinicalImpression"""
    resp = requests.post(f'{FHIR_BASE}/ClinicalImpression', json=data)
    return resp.json()

@mcp.tool
def get_clinicalimpression(resource_id: str) -> Dict[str, Any]:
    """Get a ClinicalImpression by ID. The ClinicalImpression FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ClinicalImpression"""
    resp = requests.get(f'{FHIR_BASE}/ClinicalImpression/{resource_id}')
    return resp.json()

@mcp.tool
def search_clinicalimpression(params: dict) -> Dict[str, Any]:
    """Search ClinicalImpression resources. The ClinicalImpression FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ClinicalImpression"""
    resp = requests.get(f'{FHIR_BASE}/ClinicalImpression', params=params)
    return resp.json()

@mcp.tool
def create_codesystem(data: dict) -> Dict[str, Any]:
    """Create a CodeSystem. The CodeSystem FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CodeSystem"""
    resp = requests.post(f'{FHIR_BASE}/CodeSystem', json=data)
    return resp.json()

@mcp.tool
def get_codesystem(resource_id: str) -> Dict[str, Any]:
    """Get a CodeSystem by ID. The CodeSystem FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CodeSystem"""
    resp = requests.get(f'{FHIR_BASE}/CodeSystem/{resource_id}')
    return resp.json()

@mcp.tool
def search_codesystem(params: dict) -> Dict[str, Any]:
    """Search CodeSystem resources. The CodeSystem FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CodeSystem"""
    resp = requests.get(f'{FHIR_BASE}/CodeSystem', params=params)
    return resp.json()

@mcp.tool
def create_communication(data: dict) -> Dict[str, Any]:
    """Create a Communication. The Communication FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Communication<br/>Supported profile: http://ehealth.sundhed.dk/fhir/StructureDefinition/ehealth-message"""
    resp = requests.post(f'{FHIR_BASE}/Communication', json=data)
    return resp.json()

@mcp.tool
def get_communication(resource_id: str) -> Dict[str, Any]:
    """Get a Communication by ID. The Communication FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Communication<br/>Supported profile: http://ehealth.sundhed.dk/fhir/StructureDefinition/ehealth-message"""
    resp = requests.get(f'{FHIR_BASE}/Communication/{resource_id}')
    return resp.json()

@mcp.tool
def search_communication(params: dict) -> Dict[str, Any]:
    """Search Communication resources. The Communication FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Communication<br/>Supported profile: http://ehealth.sundhed.dk/fhir/StructureDefinition/ehealth-message"""
    resp = requests.get(f'{FHIR_BASE}/Communication', params=params)
    return resp.json()

@mcp.tool
def create_communicationrequest(data: dict) -> Dict[str, Any]:
    """Create a CommunicationRequest. The CommunicationRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CommunicationRequest"""
    resp = requests.post(f'{FHIR_BASE}/CommunicationRequest', json=data)
    return resp.json()

@mcp.tool
def get_communicationrequest(resource_id: str) -> Dict[str, Any]:
    """Get a CommunicationRequest by ID. The CommunicationRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CommunicationRequest"""
    resp = requests.get(f'{FHIR_BASE}/CommunicationRequest/{resource_id}')
    return resp.json()

@mcp.tool
def search_communicationrequest(params: dict) -> Dict[str, Any]:
    """Search CommunicationRequest resources. The CommunicationRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CommunicationRequest"""
    resp = requests.get(f'{FHIR_BASE}/CommunicationRequest', params=params)
    return resp.json()

@mcp.tool
def create_compartmentdefinition(data: dict) -> Dict[str, Any]:
    """Create a CompartmentDefinition. The CompartmentDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CompartmentDefinition"""
    resp = requests.post(f'{FHIR_BASE}/CompartmentDefinition', json=data)
    return resp.json()

@mcp.tool
def get_compartmentdefinition(resource_id: str) -> Dict[str, Any]:
    """Get a CompartmentDefinition by ID. The CompartmentDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CompartmentDefinition"""
    resp = requests.get(f'{FHIR_BASE}/CompartmentDefinition/{resource_id}')
    return resp.json()

@mcp.tool
def search_compartmentdefinition(params: dict) -> Dict[str, Any]:
    """Search CompartmentDefinition resources. The CompartmentDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CompartmentDefinition"""
    resp = requests.get(f'{FHIR_BASE}/CompartmentDefinition', params=params)
    return resp.json()

@mcp.tool
def create_composition(data: dict) -> Dict[str, Any]:
    """Create a Composition. The Composition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Composition<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Composition-jurisdiction-fetal-death-report<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Composition-jurisdiction-live-birth-report<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Composition-provider-live-birth-report<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/Composition-uv-ips<br/>Supported profile: https://fhir.kbv.de/StructureDefinition/KBV_PR_EAU_Composition<br/>Supported profile: https://nrces.in/ndhm/fhir/r4/StructureDefinition/OPConsultRecord<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-composition<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shf-composition"""
    resp = requests.post(f'{FHIR_BASE}/Composition', json=data)
    return resp.json()

@mcp.tool
def get_composition(resource_id: str) -> Dict[str, Any]:
    """Get a Composition by ID. The Composition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Composition<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Composition-jurisdiction-fetal-death-report<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Composition-jurisdiction-live-birth-report<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Composition-provider-live-birth-report<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/Composition-uv-ips<br/>Supported profile: https://fhir.kbv.de/StructureDefinition/KBV_PR_EAU_Composition<br/>Supported profile: https://nrces.in/ndhm/fhir/r4/StructureDefinition/OPConsultRecord<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-composition<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shf-composition"""
    resp = requests.get(f'{FHIR_BASE}/Composition/{resource_id}')
    return resp.json()

@mcp.tool
def search_composition(params: dict) -> Dict[str, Any]:
    """Search Composition resources. The Composition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Composition<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Composition-jurisdiction-fetal-death-report<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Composition-jurisdiction-live-birth-report<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Composition-provider-live-birth-report<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/Composition-uv-ips<br/>Supported profile: https://fhir.kbv.de/StructureDefinition/KBV_PR_EAU_Composition<br/>Supported profile: https://nrces.in/ndhm/fhir/r4/StructureDefinition/OPConsultRecord<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-composition<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shf-composition"""
    resp = requests.get(f'{FHIR_BASE}/Composition', params=params)
    return resp.json()

@mcp.tool
def create_conceptmap(data: dict) -> Dict[str, Any]:
    """Create a ConceptMap. The ConceptMap FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ConceptMap<br/>Supported profile: http://phr.kanta.fi/ConceptMap"""
    resp = requests.post(f'{FHIR_BASE}/ConceptMap', json=data)
    return resp.json()

@mcp.tool
def get_conceptmap(resource_id: str) -> Dict[str, Any]:
    """Get a ConceptMap by ID. The ConceptMap FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ConceptMap<br/>Supported profile: http://phr.kanta.fi/ConceptMap"""
    resp = requests.get(f'{FHIR_BASE}/ConceptMap/{resource_id}')
    return resp.json()

@mcp.tool
def search_conceptmap(params: dict) -> Dict[str, Any]:
    """Search ConceptMap resources. The ConceptMap FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ConceptMap<br/>Supported profile: http://phr.kanta.fi/ConceptMap"""
    resp = requests.get(f'{FHIR_BASE}/ConceptMap', params=params)
    return resp.json()

@mcp.tool
def create_condition(data: dict) -> Dict[str, Any]:
    """Create a Condition. The Condition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Condition<br/>Supported profile: http://fhirr4.kids-first.io/fhir/StructureDefinition/us-core-condition<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Condition-fetal-presentation<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/Condition-uv-ips<br/>Supported profile: https://nrces.in/ndhm/fhir/r4/StructureDefinition/Condition"""
    resp = requests.post(f'{FHIR_BASE}/Condition', json=data)
    return resp.json()

@mcp.tool
def get_condition(resource_id: str) -> Dict[str, Any]:
    """Get a Condition by ID. The Condition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Condition<br/>Supported profile: http://fhirr4.kids-first.io/fhir/StructureDefinition/us-core-condition<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Condition-fetal-presentation<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/Condition-uv-ips<br/>Supported profile: https://nrces.in/ndhm/fhir/r4/StructureDefinition/Condition"""
    resp = requests.get(f'{FHIR_BASE}/Condition/{resource_id}')
    return resp.json()

@mcp.tool
def search_condition(params: dict) -> Dict[str, Any]:
    """Search Condition resources. The Condition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Condition<br/>Supported profile: http://fhirr4.kids-first.io/fhir/StructureDefinition/us-core-condition<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Condition-fetal-presentation<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/Condition-uv-ips<br/>Supported profile: https://nrces.in/ndhm/fhir/r4/StructureDefinition/Condition"""
    resp = requests.get(f'{FHIR_BASE}/Condition', params=params)
    return resp.json()

@mcp.tool
def create_consent(data: dict) -> Dict[str, Any]:
    """Create a Consent. The Consent FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Consent<br/>Supported profile: https://fhir.gevko.de/StructureDefinition/PR_OSC_Consent_LE_TE"""
    resp = requests.post(f'{FHIR_BASE}/Consent', json=data)
    return resp.json()

@mcp.tool
def get_consent(resource_id: str) -> Dict[str, Any]:
    """Get a Consent by ID. The Consent FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Consent<br/>Supported profile: https://fhir.gevko.de/StructureDefinition/PR_OSC_Consent_LE_TE"""
    resp = requests.get(f'{FHIR_BASE}/Consent/{resource_id}')
    return resp.json()

@mcp.tool
def search_consent(params: dict) -> Dict[str, Any]:
    """Search Consent resources. The Consent FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Consent<br/>Supported profile: https://fhir.gevko.de/StructureDefinition/PR_OSC_Consent_LE_TE"""
    resp = requests.get(f'{FHIR_BASE}/Consent', params=params)
    return resp.json()

@mcp.tool
def create_contract(data: dict) -> Dict[str, Any]:
    """Create a Contract. The Contract FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Contract"""
    resp = requests.post(f'{FHIR_BASE}/Contract', json=data)
    return resp.json()

@mcp.tool
def get_contract(resource_id: str) -> Dict[str, Any]:
    """Get a Contract by ID. The Contract FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Contract"""
    resp = requests.get(f'{FHIR_BASE}/Contract/{resource_id}')
    return resp.json()

@mcp.tool
def search_contract(params: dict) -> Dict[str, Any]:
    """Search Contract resources. The Contract FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Contract"""
    resp = requests.get(f'{FHIR_BASE}/Contract', params=params)
    return resp.json()

@mcp.tool
def create_coverage(data: dict) -> Dict[str, Any]:
    """Create a Coverage. The Coverage FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Coverage"""
    resp = requests.post(f'{FHIR_BASE}/Coverage', json=data)
    return resp.json()

@mcp.tool
def get_coverage(resource_id: str) -> Dict[str, Any]:
    """Get a Coverage by ID. The Coverage FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Coverage"""
    resp = requests.get(f'{FHIR_BASE}/Coverage/{resource_id}')
    return resp.json()

@mcp.tool
def search_coverage(params: dict) -> Dict[str, Any]:
    """Search Coverage resources. The Coverage FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Coverage"""
    resp = requests.get(f'{FHIR_BASE}/Coverage', params=params)
    return resp.json()

@mcp.tool
def create_coverageeligibilityrequest(data: dict) -> Dict[str, Any]:
    """Create a CoverageEligibilityRequest. The CoverageEligibilityRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CoverageEligibilityRequest"""
    resp = requests.post(f'{FHIR_BASE}/CoverageEligibilityRequest', json=data)
    return resp.json()

@mcp.tool
def get_coverageeligibilityrequest(resource_id: str) -> Dict[str, Any]:
    """Get a CoverageEligibilityRequest by ID. The CoverageEligibilityRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CoverageEligibilityRequest"""
    resp = requests.get(f'{FHIR_BASE}/CoverageEligibilityRequest/{resource_id}')
    return resp.json()

@mcp.tool
def search_coverageeligibilityrequest(params: dict) -> Dict[str, Any]:
    """Search CoverageEligibilityRequest resources. The CoverageEligibilityRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CoverageEligibilityRequest"""
    resp = requests.get(f'{FHIR_BASE}/CoverageEligibilityRequest', params=params)
    return resp.json()

@mcp.tool
def create_coverageeligibilityresponse(data: dict) -> Dict[str, Any]:
    """Create a CoverageEligibilityResponse. The CoverageEligibilityResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CoverageEligibilityResponse"""
    resp = requests.post(f'{FHIR_BASE}/CoverageEligibilityResponse', json=data)
    return resp.json()

@mcp.tool
def get_coverageeligibilityresponse(resource_id: str) -> Dict[str, Any]:
    """Get a CoverageEligibilityResponse by ID. The CoverageEligibilityResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CoverageEligibilityResponse"""
    resp = requests.get(f'{FHIR_BASE}/CoverageEligibilityResponse/{resource_id}')
    return resp.json()

@mcp.tool
def search_coverageeligibilityresponse(params: dict) -> Dict[str, Any]:
    """Search CoverageEligibilityResponse resources. The CoverageEligibilityResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/CoverageEligibilityResponse"""
    resp = requests.get(f'{FHIR_BASE}/CoverageEligibilityResponse', params=params)
    return resp.json()

@mcp.tool
def create_detectedissue(data: dict) -> Dict[str, Any]:
    """Create a DetectedIssue. The DetectedIssue FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DetectedIssue"""
    resp = requests.post(f'{FHIR_BASE}/DetectedIssue', json=data)
    return resp.json()

@mcp.tool
def get_detectedissue(resource_id: str) -> Dict[str, Any]:
    """Get a DetectedIssue by ID. The DetectedIssue FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DetectedIssue"""
    resp = requests.get(f'{FHIR_BASE}/DetectedIssue/{resource_id}')
    return resp.json()

@mcp.tool
def search_detectedissue(params: dict) -> Dict[str, Any]:
    """Search DetectedIssue resources. The DetectedIssue FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DetectedIssue"""
    resp = requests.get(f'{FHIR_BASE}/DetectedIssue', params=params)
    return resp.json()

@mcp.tool
def create_device(data: dict) -> Dict[str, Any]:
    """Create a Device. The Device FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Device<br/>Supported profile: http://example.org/fhir/dossi/StructureDefinition/dossi-device<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-implantable-device<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/device-softwaresystem-cqfm"""
    resp = requests.post(f'{FHIR_BASE}/Device', json=data)
    return resp.json()

@mcp.tool
def get_device(resource_id: str) -> Dict[str, Any]:
    """Get a Device by ID. The Device FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Device<br/>Supported profile: http://example.org/fhir/dossi/StructureDefinition/dossi-device<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-implantable-device<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/device-softwaresystem-cqfm"""
    resp = requests.get(f'{FHIR_BASE}/Device/{resource_id}')
    return resp.json()

@mcp.tool
def search_device(params: dict) -> Dict[str, Any]:
    """Search Device resources. The Device FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Device<br/>Supported profile: http://example.org/fhir/dossi/StructureDefinition/dossi-device<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-implantable-device<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/device-softwaresystem-cqfm"""
    resp = requests.get(f'{FHIR_BASE}/Device', params=params)
    return resp.json()

@mcp.tool
def create_devicedefinition(data: dict) -> Dict[str, Any]:
    """Create a DeviceDefinition. The DeviceDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DeviceDefinition<br/>Supported profile: http://example.org/fhir/dossi/StructureDefinition/dossi-devicedefinition"""
    resp = requests.post(f'{FHIR_BASE}/DeviceDefinition', json=data)
    return resp.json()

@mcp.tool
def get_devicedefinition(resource_id: str) -> Dict[str, Any]:
    """Get a DeviceDefinition by ID. The DeviceDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DeviceDefinition<br/>Supported profile: http://example.org/fhir/dossi/StructureDefinition/dossi-devicedefinition"""
    resp = requests.get(f'{FHIR_BASE}/DeviceDefinition/{resource_id}')
    return resp.json()

@mcp.tool
def search_devicedefinition(params: dict) -> Dict[str, Any]:
    """Search DeviceDefinition resources. The DeviceDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DeviceDefinition<br/>Supported profile: http://example.org/fhir/dossi/StructureDefinition/dossi-devicedefinition"""
    resp = requests.get(f'{FHIR_BASE}/DeviceDefinition', params=params)
    return resp.json()

@mcp.tool
def create_devicemetric(data: dict) -> Dict[str, Any]:
    """Create a DeviceMetric. The DeviceMetric FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DeviceMetric"""
    resp = requests.post(f'{FHIR_BASE}/DeviceMetric', json=data)
    return resp.json()

@mcp.tool
def get_devicemetric(resource_id: str) -> Dict[str, Any]:
    """Get a DeviceMetric by ID. The DeviceMetric FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DeviceMetric"""
    resp = requests.get(f'{FHIR_BASE}/DeviceMetric/{resource_id}')
    return resp.json()

@mcp.tool
def search_devicemetric(params: dict) -> Dict[str, Any]:
    """Search DeviceMetric resources. The DeviceMetric FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DeviceMetric"""
    resp = requests.get(f'{FHIR_BASE}/DeviceMetric', params=params)
    return resp.json()

@mcp.tool
def create_devicerequest(data: dict) -> Dict[str, Any]:
    """Create a DeviceRequest. The DeviceRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DeviceRequest<br/>Supported profile: http://example.org/fhir/dossi/StructureDefinition/dossi-devicerequest"""
    resp = requests.post(f'{FHIR_BASE}/DeviceRequest', json=data)
    return resp.json()

@mcp.tool
def get_devicerequest(resource_id: str) -> Dict[str, Any]:
    """Get a DeviceRequest by ID. The DeviceRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DeviceRequest<br/>Supported profile: http://example.org/fhir/dossi/StructureDefinition/dossi-devicerequest"""
    resp = requests.get(f'{FHIR_BASE}/DeviceRequest/{resource_id}')
    return resp.json()

@mcp.tool
def search_devicerequest(params: dict) -> Dict[str, Any]:
    """Search DeviceRequest resources. The DeviceRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DeviceRequest<br/>Supported profile: http://example.org/fhir/dossi/StructureDefinition/dossi-devicerequest"""
    resp = requests.get(f'{FHIR_BASE}/DeviceRequest', params=params)
    return resp.json()

@mcp.tool
def create_deviceusestatement(data: dict) -> Dict[str, Any]:
    """Create a DeviceUseStatement. The DeviceUseStatement FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DeviceUseStatement<br/>Supported profile: http://example.org/fhir/dossi/StructureDefinition/dossi-deviceusestatement<br/>Supported profile: https://fhir.hl7.at/elga-austrianpatientsummary-r4/StructureDefinition/at-aps-deviceusestatement"""
    resp = requests.post(f'{FHIR_BASE}/DeviceUseStatement', json=data)
    return resp.json()

@mcp.tool
def get_deviceusestatement(resource_id: str) -> Dict[str, Any]:
    """Get a DeviceUseStatement by ID. The DeviceUseStatement FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DeviceUseStatement<br/>Supported profile: http://example.org/fhir/dossi/StructureDefinition/dossi-deviceusestatement<br/>Supported profile: https://fhir.hl7.at/elga-austrianpatientsummary-r4/StructureDefinition/at-aps-deviceusestatement"""
    resp = requests.get(f'{FHIR_BASE}/DeviceUseStatement/{resource_id}')
    return resp.json()

@mcp.tool
def search_deviceusestatement(params: dict) -> Dict[str, Any]:
    """Search DeviceUseStatement resources. The DeviceUseStatement FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DeviceUseStatement<br/>Supported profile: http://example.org/fhir/dossi/StructureDefinition/dossi-deviceusestatement<br/>Supported profile: https://fhir.hl7.at/elga-austrianpatientsummary-r4/StructureDefinition/at-aps-deviceusestatement"""
    resp = requests.get(f'{FHIR_BASE}/DeviceUseStatement', params=params)
    return resp.json()

@mcp.tool
def create_diagnosticreport(data: dict) -> Dict[str, Any]:
    """Create a DiagnosticReport. The DiagnosticReport FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DiagnosticReport<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-diagnosticreport-lab<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-diagnosticreport-note<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/genomics-report"""
    resp = requests.post(f'{FHIR_BASE}/DiagnosticReport', json=data)
    return resp.json()

@mcp.tool
def get_diagnosticreport(resource_id: str) -> Dict[str, Any]:
    """Get a DiagnosticReport by ID. The DiagnosticReport FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DiagnosticReport<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-diagnosticreport-lab<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-diagnosticreport-note<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/genomics-report"""
    resp = requests.get(f'{FHIR_BASE}/DiagnosticReport/{resource_id}')
    return resp.json()

@mcp.tool
def search_diagnosticreport(params: dict) -> Dict[str, Any]:
    """Search DiagnosticReport resources. The DiagnosticReport FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DiagnosticReport<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-diagnosticreport-lab<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-diagnosticreport-note<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/genomics-report"""
    resp = requests.get(f'{FHIR_BASE}/DiagnosticReport', params=params)
    return resp.json()

@mcp.tool
def create_documentmanifest(data: dict) -> Dict[str, Any]:
    """Create a DocumentManifest. The DocumentManifest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DocumentManifest<br/>Supported profile: http://fhir.gevko.de/fhir/StructureDefinition/EVoDocumentManifest"""
    resp = requests.post(f'{FHIR_BASE}/DocumentManifest', json=data)
    return resp.json()

@mcp.tool
def get_documentmanifest(resource_id: str) -> Dict[str, Any]:
    """Get a DocumentManifest by ID. The DocumentManifest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DocumentManifest<br/>Supported profile: http://fhir.gevko.de/fhir/StructureDefinition/EVoDocumentManifest"""
    resp = requests.get(f'{FHIR_BASE}/DocumentManifest/{resource_id}')
    return resp.json()

@mcp.tool
def search_documentmanifest(params: dict) -> Dict[str, Any]:
    """Search DocumentManifest resources. The DocumentManifest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DocumentManifest<br/>Supported profile: http://fhir.gevko.de/fhir/StructureDefinition/EVoDocumentManifest"""
    resp = requests.get(f'{FHIR_BASE}/DocumentManifest', params=params)
    return resp.json()

@mcp.tool
def create_documentreference(data: dict) -> Dict[str, Any]:
    """Create a DocumentReference. The DocumentReference FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DocumentReference<br/>Supported profile: http://fhir.gevko.de/fhir/StructureDefinition/EVoDocumentReference<br/>Supported profile: http://gev.de/fhir/StructureDefinition/RepoDocumentReference<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-documentreference"""
    resp = requests.post(f'{FHIR_BASE}/DocumentReference', json=data)
    return resp.json()

@mcp.tool
def get_documentreference(resource_id: str) -> Dict[str, Any]:
    """Get a DocumentReference by ID. The DocumentReference FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DocumentReference<br/>Supported profile: http://fhir.gevko.de/fhir/StructureDefinition/EVoDocumentReference<br/>Supported profile: http://gev.de/fhir/StructureDefinition/RepoDocumentReference<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-documentreference"""
    resp = requests.get(f'{FHIR_BASE}/DocumentReference/{resource_id}')
    return resp.json()

@mcp.tool
def search_documentreference(params: dict) -> Dict[str, Any]:
    """Search DocumentReference resources. The DocumentReference FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/DocumentReference<br/>Supported profile: http://fhir.gevko.de/fhir/StructureDefinition/EVoDocumentReference<br/>Supported profile: http://gev.de/fhir/StructureDefinition/RepoDocumentReference<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-documentreference"""
    resp = requests.get(f'{FHIR_BASE}/DocumentReference', params=params)
    return resp.json()

@mcp.tool
def create_effectevidencesynthesis(data: dict) -> Dict[str, Any]:
    """Create a EffectEvidenceSynthesis. The EffectEvidenceSynthesis FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EffectEvidenceSynthesis"""
    resp = requests.post(f'{FHIR_BASE}/EffectEvidenceSynthesis', json=data)
    return resp.json()

@mcp.tool
def get_effectevidencesynthesis(resource_id: str) -> Dict[str, Any]:
    """Get a EffectEvidenceSynthesis by ID. The EffectEvidenceSynthesis FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EffectEvidenceSynthesis"""
    resp = requests.get(f'{FHIR_BASE}/EffectEvidenceSynthesis/{resource_id}')
    return resp.json()

@mcp.tool
def search_effectevidencesynthesis(params: dict) -> Dict[str, Any]:
    """Search EffectEvidenceSynthesis resources. The EffectEvidenceSynthesis FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EffectEvidenceSynthesis"""
    resp = requests.get(f'{FHIR_BASE}/EffectEvidenceSynthesis', params=params)
    return resp.json()

@mcp.tool
def create_encounter(data: dict) -> Dict[str, Any]:
    """Create a Encounter. The Encounter FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Encounter<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter"""
    resp = requests.post(f'{FHIR_BASE}/Encounter', json=data)
    return resp.json()

@mcp.tool
def get_encounter(resource_id: str) -> Dict[str, Any]:
    """Get a Encounter by ID. The Encounter FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Encounter<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter"""
    resp = requests.get(f'{FHIR_BASE}/Encounter/{resource_id}')
    return resp.json()

@mcp.tool
def search_encounter(params: dict) -> Dict[str, Any]:
    """Search Encounter resources. The Encounter FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Encounter<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter"""
    resp = requests.get(f'{FHIR_BASE}/Encounter', params=params)
    return resp.json()

@mcp.tool
def create_endpoint(data: dict) -> Dict[str, Any]:
    """Create a Endpoint. The Endpoint FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Endpoint"""
    resp = requests.post(f'{FHIR_BASE}/Endpoint', json=data)
    return resp.json()

@mcp.tool
def get_endpoint(resource_id: str) -> Dict[str, Any]:
    """Get a Endpoint by ID. The Endpoint FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Endpoint"""
    resp = requests.get(f'{FHIR_BASE}/Endpoint/{resource_id}')
    return resp.json()

@mcp.tool
def search_endpoint(params: dict) -> Dict[str, Any]:
    """Search Endpoint resources. The Endpoint FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Endpoint"""
    resp = requests.get(f'{FHIR_BASE}/Endpoint', params=params)
    return resp.json()

@mcp.tool
def create_enrollmentrequest(data: dict) -> Dict[str, Any]:
    """Create a EnrollmentRequest. The EnrollmentRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EnrollmentRequest"""
    resp = requests.post(f'{FHIR_BASE}/EnrollmentRequest', json=data)
    return resp.json()

@mcp.tool
def get_enrollmentrequest(resource_id: str) -> Dict[str, Any]:
    """Get a EnrollmentRequest by ID. The EnrollmentRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EnrollmentRequest"""
    resp = requests.get(f'{FHIR_BASE}/EnrollmentRequest/{resource_id}')
    return resp.json()

@mcp.tool
def search_enrollmentrequest(params: dict) -> Dict[str, Any]:
    """Search EnrollmentRequest resources. The EnrollmentRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EnrollmentRequest"""
    resp = requests.get(f'{FHIR_BASE}/EnrollmentRequest', params=params)
    return resp.json()

@mcp.tool
def create_enrollmentresponse(data: dict) -> Dict[str, Any]:
    """Create a EnrollmentResponse. The EnrollmentResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EnrollmentResponse"""
    resp = requests.post(f'{FHIR_BASE}/EnrollmentResponse', json=data)
    return resp.json()

@mcp.tool
def get_enrollmentresponse(resource_id: str) -> Dict[str, Any]:
    """Get a EnrollmentResponse by ID. The EnrollmentResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EnrollmentResponse"""
    resp = requests.get(f'{FHIR_BASE}/EnrollmentResponse/{resource_id}')
    return resp.json()

@mcp.tool
def search_enrollmentresponse(params: dict) -> Dict[str, Any]:
    """Search EnrollmentResponse resources. The EnrollmentResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EnrollmentResponse"""
    resp = requests.get(f'{FHIR_BASE}/EnrollmentResponse', params=params)
    return resp.json()

@mcp.tool
def create_episodeofcare(data: dict) -> Dict[str, Any]:
    """Create a EpisodeOfCare. The EpisodeOfCare FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EpisodeOfCare<br/>Supported profile: http://hl7.dk/fhir/core/StructureDefinition/dk-core-episodeOfCare"""
    resp = requests.post(f'{FHIR_BASE}/EpisodeOfCare', json=data)
    return resp.json()

@mcp.tool
def get_episodeofcare(resource_id: str) -> Dict[str, Any]:
    """Get a EpisodeOfCare by ID. The EpisodeOfCare FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EpisodeOfCare<br/>Supported profile: http://hl7.dk/fhir/core/StructureDefinition/dk-core-episodeOfCare"""
    resp = requests.get(f'{FHIR_BASE}/EpisodeOfCare/{resource_id}')
    return resp.json()

@mcp.tool
def search_episodeofcare(params: dict) -> Dict[str, Any]:
    """Search EpisodeOfCare resources. The EpisodeOfCare FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EpisodeOfCare<br/>Supported profile: http://hl7.dk/fhir/core/StructureDefinition/dk-core-episodeOfCare"""
    resp = requests.get(f'{FHIR_BASE}/EpisodeOfCare', params=params)
    return resp.json()

@mcp.tool
def create_eventdefinition(data: dict) -> Dict[str, Any]:
    """Create a EventDefinition. The EventDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EventDefinition"""
    resp = requests.post(f'{FHIR_BASE}/EventDefinition', json=data)
    return resp.json()

@mcp.tool
def get_eventdefinition(resource_id: str) -> Dict[str, Any]:
    """Get a EventDefinition by ID. The EventDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EventDefinition"""
    resp = requests.get(f'{FHIR_BASE}/EventDefinition/{resource_id}')
    return resp.json()

@mcp.tool
def search_eventdefinition(params: dict) -> Dict[str, Any]:
    """Search EventDefinition resources. The EventDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EventDefinition"""
    resp = requests.get(f'{FHIR_BASE}/EventDefinition', params=params)
    return resp.json()

@mcp.tool
def create_evidence(data: dict) -> Dict[str, Any]:
    """Create a Evidence. The Evidence FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Evidence"""
    resp = requests.post(f'{FHIR_BASE}/Evidence', json=data)
    return resp.json()

@mcp.tool
def get_evidence(resource_id: str) -> Dict[str, Any]:
    """Get a Evidence by ID. The Evidence FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Evidence"""
    resp = requests.get(f'{FHIR_BASE}/Evidence/{resource_id}')
    return resp.json()

@mcp.tool
def search_evidence(params: dict) -> Dict[str, Any]:
    """Search Evidence resources. The Evidence FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Evidence"""
    resp = requests.get(f'{FHIR_BASE}/Evidence', params=params)
    return resp.json()

@mcp.tool
def create_evidencevariable(data: dict) -> Dict[str, Any]:
    """Create a EvidenceVariable. The EvidenceVariable FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EvidenceVariable"""
    resp = requests.post(f'{FHIR_BASE}/EvidenceVariable', json=data)
    return resp.json()

@mcp.tool
def get_evidencevariable(resource_id: str) -> Dict[str, Any]:
    """Get a EvidenceVariable by ID. The EvidenceVariable FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EvidenceVariable"""
    resp = requests.get(f'{FHIR_BASE}/EvidenceVariable/{resource_id}')
    return resp.json()

@mcp.tool
def search_evidencevariable(params: dict) -> Dict[str, Any]:
    """Search EvidenceVariable resources. The EvidenceVariable FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/EvidenceVariable"""
    resp = requests.get(f'{FHIR_BASE}/EvidenceVariable', params=params)
    return resp.json()

@mcp.tool
def create_examplescenario(data: dict) -> Dict[str, Any]:
    """Create a ExampleScenario. The ExampleScenario FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ExampleScenario"""
    resp = requests.post(f'{FHIR_BASE}/ExampleScenario', json=data)
    return resp.json()

@mcp.tool
def get_examplescenario(resource_id: str) -> Dict[str, Any]:
    """Get a ExampleScenario by ID. The ExampleScenario FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ExampleScenario"""
    resp = requests.get(f'{FHIR_BASE}/ExampleScenario/{resource_id}')
    return resp.json()

@mcp.tool
def search_examplescenario(params: dict) -> Dict[str, Any]:
    """Search ExampleScenario resources. The ExampleScenario FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ExampleScenario"""
    resp = requests.get(f'{FHIR_BASE}/ExampleScenario', params=params)
    return resp.json()

@mcp.tool
def create_explanationofbenefit(data: dict) -> Dict[str, Any]:
    """Create a ExplanationOfBenefit. The ExplanationOfBenefit FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit"""
    resp = requests.post(f'{FHIR_BASE}/ExplanationOfBenefit', json=data)
    return resp.json()

@mcp.tool
def get_explanationofbenefit(resource_id: str) -> Dict[str, Any]:
    """Get a ExplanationOfBenefit by ID. The ExplanationOfBenefit FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit"""
    resp = requests.get(f'{FHIR_BASE}/ExplanationOfBenefit/{resource_id}')
    return resp.json()

@mcp.tool
def search_explanationofbenefit(params: dict) -> Dict[str, Any]:
    """Search ExplanationOfBenefit resources. The ExplanationOfBenefit FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ExplanationOfBenefit"""
    resp = requests.get(f'{FHIR_BASE}/ExplanationOfBenefit', params=params)
    return resp.json()

@mcp.tool
def create_familymemberhistory(data: dict) -> Dict[str, Any]:
    """Create a FamilyMemberHistory. The FamilyMemberHistory FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory"""
    resp = requests.post(f'{FHIR_BASE}/FamilyMemberHistory', json=data)
    return resp.json()

@mcp.tool
def get_familymemberhistory(resource_id: str) -> Dict[str, Any]:
    """Get a FamilyMemberHistory by ID. The FamilyMemberHistory FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory"""
    resp = requests.get(f'{FHIR_BASE}/FamilyMemberHistory/{resource_id}')
    return resp.json()

@mcp.tool
def search_familymemberhistory(params: dict) -> Dict[str, Any]:
    """Search FamilyMemberHistory resources. The FamilyMemberHistory FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory"""
    resp = requests.get(f'{FHIR_BASE}/FamilyMemberHistory', params=params)
    return resp.json()

@mcp.tool
def create_flag(data: dict) -> Dict[str, Any]:
    """Create a Flag. The Flag FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Flag"""
    resp = requests.post(f'{FHIR_BASE}/Flag', json=data)
    return resp.json()

@mcp.tool
def get_flag(resource_id: str) -> Dict[str, Any]:
    """Get a Flag by ID. The Flag FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Flag"""
    resp = requests.get(f'{FHIR_BASE}/Flag/{resource_id}')
    return resp.json()

@mcp.tool
def search_flag(params: dict) -> Dict[str, Any]:
    """Search Flag resources. The Flag FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Flag"""
    resp = requests.get(f'{FHIR_BASE}/Flag', params=params)
    return resp.json()

@mcp.tool
def create_goal(data: dict) -> Dict[str, Any]:
    """Create a Goal. The Goal FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Goal<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-goal"""
    resp = requests.post(f'{FHIR_BASE}/Goal', json=data)
    return resp.json()

@mcp.tool
def get_goal(resource_id: str) -> Dict[str, Any]:
    """Get a Goal by ID. The Goal FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Goal<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-goal"""
    resp = requests.get(f'{FHIR_BASE}/Goal/{resource_id}')
    return resp.json()

@mcp.tool
def search_goal(params: dict) -> Dict[str, Any]:
    """Search Goal resources. The Goal FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Goal<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-goal"""
    resp = requests.get(f'{FHIR_BASE}/Goal', params=params)
    return resp.json()

@mcp.tool
def create_graphdefinition(data: dict) -> Dict[str, Any]:
    """Create a GraphDefinition. The GraphDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/GraphDefinition<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shf-graphdefinition"""
    resp = requests.post(f'{FHIR_BASE}/GraphDefinition', json=data)
    return resp.json()

@mcp.tool
def get_graphdefinition(resource_id: str) -> Dict[str, Any]:
    """Get a GraphDefinition by ID. The GraphDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/GraphDefinition<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shf-graphdefinition"""
    resp = requests.get(f'{FHIR_BASE}/GraphDefinition/{resource_id}')
    return resp.json()

@mcp.tool
def search_graphdefinition(params: dict) -> Dict[str, Any]:
    """Search GraphDefinition resources. The GraphDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/GraphDefinition<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shf-graphdefinition"""
    resp = requests.get(f'{FHIR_BASE}/GraphDefinition', params=params)
    return resp.json()

@mcp.tool
def create_group(data: dict) -> Dict[str, Any]:
    """Create a Group. The Group FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Group"""
    resp = requests.post(f'{FHIR_BASE}/Group', json=data)
    return resp.json()

@mcp.tool
def get_group(resource_id: str) -> Dict[str, Any]:
    """Get a Group by ID. The Group FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Group"""
    resp = requests.get(f'{FHIR_BASE}/Group/{resource_id}')
    return resp.json()

@mcp.tool
def search_group(params: dict) -> Dict[str, Any]:
    """Search Group resources. The Group FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Group"""
    resp = requests.get(f'{FHIR_BASE}/Group', params=params)
    return resp.json()

@mcp.tool
def create_guidanceresponse(data: dict) -> Dict[str, Any]:
    """Create a GuidanceResponse. The GuidanceResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/GuidanceResponse"""
    resp = requests.post(f'{FHIR_BASE}/GuidanceResponse', json=data)
    return resp.json()

@mcp.tool
def get_guidanceresponse(resource_id: str) -> Dict[str, Any]:
    """Get a GuidanceResponse by ID. The GuidanceResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/GuidanceResponse"""
    resp = requests.get(f'{FHIR_BASE}/GuidanceResponse/{resource_id}')
    return resp.json()

@mcp.tool
def search_guidanceresponse(params: dict) -> Dict[str, Any]:
    """Search GuidanceResponse resources. The GuidanceResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/GuidanceResponse"""
    resp = requests.get(f'{FHIR_BASE}/GuidanceResponse', params=params)
    return resp.json()

@mcp.tool
def create_healthcareservice(data: dict) -> Dict[str, Any]:
    """Create a HealthcareService. The HealthcareService FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/HealthcareService<br/>Supported profile: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-HealthcareService<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.HealthcareService"""
    resp = requests.post(f'{FHIR_BASE}/HealthcareService', json=data)
    return resp.json()

@mcp.tool
def get_healthcareservice(resource_id: str) -> Dict[str, Any]:
    """Get a HealthcareService by ID. The HealthcareService FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/HealthcareService<br/>Supported profile: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-HealthcareService<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.HealthcareService"""
    resp = requests.get(f'{FHIR_BASE}/HealthcareService/{resource_id}')
    return resp.json()

@mcp.tool
def search_healthcareservice(params: dict) -> Dict[str, Any]:
    """Search HealthcareService resources. The HealthcareService FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/HealthcareService<br/>Supported profile: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-HealthcareService<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.HealthcareService"""
    resp = requests.get(f'{FHIR_BASE}/HealthcareService', params=params)
    return resp.json()

@mcp.tool
def create_imagingstudy(data: dict) -> Dict[str, Any]:
    """Create a ImagingStudy. The ImagingStudy FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ImagingStudy"""
    resp = requests.post(f'{FHIR_BASE}/ImagingStudy', json=data)
    return resp.json()

@mcp.tool
def get_imagingstudy(resource_id: str) -> Dict[str, Any]:
    """Get a ImagingStudy by ID. The ImagingStudy FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ImagingStudy"""
    resp = requests.get(f'{FHIR_BASE}/ImagingStudy/{resource_id}')
    return resp.json()

@mcp.tool
def search_imagingstudy(params: dict) -> Dict[str, Any]:
    """Search ImagingStudy resources. The ImagingStudy FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ImagingStudy"""
    resp = requests.get(f'{FHIR_BASE}/ImagingStudy', params=params)
    return resp.json()

@mcp.tool
def create_immunization(data: dict) -> Dict[str, Any]:
    """Create a Immunization. The Immunization FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Immunization<br/>Supported profile: http://build.fhir.org/ig/hitstdio/sample-ig/StructureDefinition/vaccination-credential-immunization<br/>Supported profile: http://example.org/fhir/StructureDefinition/KRImmunization<br/>Supported profile: http://hitstdio.ntunhs.edu.tw/ig/lab/smarthealthcards-vaccination/StructureDefinition/vaccination-credential-immunization<br/>Supported profile: http://hl7.eu/fhir/ig/dgc/StructureDefinition/Immunization-dgc<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-immunization<br/>Supported profile: http://hl7.org/fhir/uv/smarthealthcards-vaccination/StructureDefinition/vaccination-credential-immunization<br/>Supported profile: https://jembi.github.io/covid19-immunization-ig//StructureDefinition/covid19-immunization"""
    resp = requests.post(f'{FHIR_BASE}/Immunization', json=data)
    return resp.json()

@mcp.tool
def get_immunization(resource_id: str) -> Dict[str, Any]:
    """Get a Immunization by ID. The Immunization FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Immunization<br/>Supported profile: http://build.fhir.org/ig/hitstdio/sample-ig/StructureDefinition/vaccination-credential-immunization<br/>Supported profile: http://example.org/fhir/StructureDefinition/KRImmunization<br/>Supported profile: http://hitstdio.ntunhs.edu.tw/ig/lab/smarthealthcards-vaccination/StructureDefinition/vaccination-credential-immunization<br/>Supported profile: http://hl7.eu/fhir/ig/dgc/StructureDefinition/Immunization-dgc<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-immunization<br/>Supported profile: http://hl7.org/fhir/uv/smarthealthcards-vaccination/StructureDefinition/vaccination-credential-immunization<br/>Supported profile: https://jembi.github.io/covid19-immunization-ig//StructureDefinition/covid19-immunization"""
    resp = requests.get(f'{FHIR_BASE}/Immunization/{resource_id}')
    return resp.json()

@mcp.tool
def search_immunization(params: dict) -> Dict[str, Any]:
    """Search Immunization resources. The Immunization FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Immunization<br/>Supported profile: http://build.fhir.org/ig/hitstdio/sample-ig/StructureDefinition/vaccination-credential-immunization<br/>Supported profile: http://example.org/fhir/StructureDefinition/KRImmunization<br/>Supported profile: http://hitstdio.ntunhs.edu.tw/ig/lab/smarthealthcards-vaccination/StructureDefinition/vaccination-credential-immunization<br/>Supported profile: http://hl7.eu/fhir/ig/dgc/StructureDefinition/Immunization-dgc<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-immunization<br/>Supported profile: http://hl7.org/fhir/uv/smarthealthcards-vaccination/StructureDefinition/vaccination-credential-immunization<br/>Supported profile: https://jembi.github.io/covid19-immunization-ig//StructureDefinition/covid19-immunization"""
    resp = requests.get(f'{FHIR_BASE}/Immunization', params=params)
    return resp.json()

@mcp.tool
def create_immunizationevaluation(data: dict) -> Dict[str, Any]:
    """Create a ImmunizationEvaluation. The ImmunizationEvaluation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation"""
    resp = requests.post(f'{FHIR_BASE}/ImmunizationEvaluation', json=data)
    return resp.json()

@mcp.tool
def get_immunizationevaluation(resource_id: str) -> Dict[str, Any]:
    """Get a ImmunizationEvaluation by ID. The ImmunizationEvaluation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation"""
    resp = requests.get(f'{FHIR_BASE}/ImmunizationEvaluation/{resource_id}')
    return resp.json()

@mcp.tool
def search_immunizationevaluation(params: dict) -> Dict[str, Any]:
    """Search ImmunizationEvaluation resources. The ImmunizationEvaluation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ImmunizationEvaluation"""
    resp = requests.get(f'{FHIR_BASE}/ImmunizationEvaluation', params=params)
    return resp.json()

@mcp.tool
def create_immunizationrecommendation(data: dict) -> Dict[str, Any]:
    """Create a ImmunizationRecommendation. The ImmunizationRecommendation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation"""
    resp = requests.post(f'{FHIR_BASE}/ImmunizationRecommendation', json=data)
    return resp.json()

@mcp.tool
def get_immunizationrecommendation(resource_id: str) -> Dict[str, Any]:
    """Get a ImmunizationRecommendation by ID. The ImmunizationRecommendation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation"""
    resp = requests.get(f'{FHIR_BASE}/ImmunizationRecommendation/{resource_id}')
    return resp.json()

@mcp.tool
def search_immunizationrecommendation(params: dict) -> Dict[str, Any]:
    """Search ImmunizationRecommendation resources. The ImmunizationRecommendation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ImmunizationRecommendation"""
    resp = requests.get(f'{FHIR_BASE}/ImmunizationRecommendation', params=params)
    return resp.json()

@mcp.tool
def create_implementationguide(data: dict) -> Dict[str, Any]:
    """Create a ImplementationGuide. The ImplementationGuide FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ImplementationGuide"""
    resp = requests.post(f'{FHIR_BASE}/ImplementationGuide', json=data)
    return resp.json()

@mcp.tool
def get_implementationguide(resource_id: str) -> Dict[str, Any]:
    """Get a ImplementationGuide by ID. The ImplementationGuide FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ImplementationGuide"""
    resp = requests.get(f'{FHIR_BASE}/ImplementationGuide/{resource_id}')
    return resp.json()

@mcp.tool
def search_implementationguide(params: dict) -> Dict[str, Any]:
    """Search ImplementationGuide resources. The ImplementationGuide FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ImplementationGuide"""
    resp = requests.get(f'{FHIR_BASE}/ImplementationGuide', params=params)
    return resp.json()

@mcp.tool
def create_insuranceplan(data: dict) -> Dict[str, Any]:
    """Create a InsurancePlan. The InsurancePlan FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/InsurancePlan"""
    resp = requests.post(f'{FHIR_BASE}/InsurancePlan', json=data)
    return resp.json()

@mcp.tool
def get_insuranceplan(resource_id: str) -> Dict[str, Any]:
    """Get a InsurancePlan by ID. The InsurancePlan FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/InsurancePlan"""
    resp = requests.get(f'{FHIR_BASE}/InsurancePlan/{resource_id}')
    return resp.json()

@mcp.tool
def search_insuranceplan(params: dict) -> Dict[str, Any]:
    """Search InsurancePlan resources. The InsurancePlan FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/InsurancePlan"""
    resp = requests.get(f'{FHIR_BASE}/InsurancePlan', params=params)
    return resp.json()

@mcp.tool
def create_invoice(data: dict) -> Dict[str, Any]:
    """Create a Invoice. The Invoice FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Invoice"""
    resp = requests.post(f'{FHIR_BASE}/Invoice', json=data)
    return resp.json()

@mcp.tool
def get_invoice(resource_id: str) -> Dict[str, Any]:
    """Get a Invoice by ID. The Invoice FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Invoice"""
    resp = requests.get(f'{FHIR_BASE}/Invoice/{resource_id}')
    return resp.json()

@mcp.tool
def search_invoice(params: dict) -> Dict[str, Any]:
    """Search Invoice resources. The Invoice FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Invoice"""
    resp = requests.get(f'{FHIR_BASE}/Invoice', params=params)
    return resp.json()

@mcp.tool
def create_library(data: dict) -> Dict[str, Any]:
    """Create a Library. The Library FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Library<br/>Supported profile: http://fkcfhir.org/fhir/StructureDefinition/Catalog<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/computable-library-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/executable-library-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/library-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/publishable-library-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/quality-program-cqfm<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/PublicHealthMeasureLibrary"""
    resp = requests.post(f'{FHIR_BASE}/Library', json=data)
    return resp.json()

@mcp.tool
def get_library(resource_id: str) -> Dict[str, Any]:
    """Get a Library by ID. The Library FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Library<br/>Supported profile: http://fkcfhir.org/fhir/StructureDefinition/Catalog<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/computable-library-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/executable-library-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/library-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/publishable-library-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/quality-program-cqfm<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/PublicHealthMeasureLibrary"""
    resp = requests.get(f'{FHIR_BASE}/Library/{resource_id}')
    return resp.json()

@mcp.tool
def search_library(params: dict) -> Dict[str, Any]:
    """Search Library resources. The Library FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Library<br/>Supported profile: http://fkcfhir.org/fhir/StructureDefinition/Catalog<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/computable-library-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/executable-library-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/library-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/publishable-library-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/quality-program-cqfm<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/PublicHealthMeasureLibrary"""
    resp = requests.get(f'{FHIR_BASE}/Library', params=params)
    return resp.json()

@mcp.tool
def create_linkage(data: dict) -> Dict[str, Any]:
    """Create a Linkage. The Linkage FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Linkage"""
    resp = requests.post(f'{FHIR_BASE}/Linkage', json=data)
    return resp.json()

@mcp.tool
def get_linkage(resource_id: str) -> Dict[str, Any]:
    """Get a Linkage by ID. The Linkage FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Linkage"""
    resp = requests.get(f'{FHIR_BASE}/Linkage/{resource_id}')
    return resp.json()

@mcp.tool
def search_linkage(params: dict) -> Dict[str, Any]:
    """Search Linkage resources. The Linkage FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Linkage"""
    resp = requests.get(f'{FHIR_BASE}/Linkage', params=params)
    return resp.json()

@mcp.tool
def create_list(data: dict) -> Dict[str, Any]:
    """Create a List. The List FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/List<br/>Supported profile: http://hl7.org/fhir/us/Davinci-drug-formulary/StructureDefinition/usdf-CoveragePlan"""
    resp = requests.post(f'{FHIR_BASE}/List', json=data)
    return resp.json()

@mcp.tool
def get_list(resource_id: str) -> Dict[str, Any]:
    """Get a List by ID. The List FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/List<br/>Supported profile: http://hl7.org/fhir/us/Davinci-drug-formulary/StructureDefinition/usdf-CoveragePlan"""
    resp = requests.get(f'{FHIR_BASE}/List/{resource_id}')
    return resp.json()

@mcp.tool
def search_list(params: dict) -> Dict[str, Any]:
    """Search List resources. The List FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/List<br/>Supported profile: http://hl7.org/fhir/us/Davinci-drug-formulary/StructureDefinition/usdf-CoveragePlan"""
    resp = requests.get(f'{FHIR_BASE}/List', params=params)
    return resp.json()

@mcp.tool
def create_location(data: dict) -> Dict[str, Any]:
    """Create a Location. The Location FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Location<br/>Supported profile: http://healshealthcare.com/fhir/StructureDefinition/Location<br/>Supported profile: http://healshealthcare.com/fhir/StructureDefinition/LocationDistrict<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-location<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.FacilityLocation<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.JurisdictionLocation<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.Location<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.LocationDistance"""
    resp = requests.post(f'{FHIR_BASE}/Location', json=data)
    return resp.json()

@mcp.tool
def get_location(resource_id: str) -> Dict[str, Any]:
    """Get a Location by ID. The Location FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Location<br/>Supported profile: http://healshealthcare.com/fhir/StructureDefinition/Location<br/>Supported profile: http://healshealthcare.com/fhir/StructureDefinition/LocationDistrict<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-location<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.FacilityLocation<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.JurisdictionLocation<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.Location<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.LocationDistance"""
    resp = requests.get(f'{FHIR_BASE}/Location/{resource_id}')
    return resp.json()

@mcp.tool
def search_location(params: dict) -> Dict[str, Any]:
    """Search Location resources. The Location FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Location<br/>Supported profile: http://healshealthcare.com/fhir/StructureDefinition/Location<br/>Supported profile: http://healshealthcare.com/fhir/StructureDefinition/LocationDistrict<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-location<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.FacilityLocation<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.JurisdictionLocation<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.Location<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.LocationDistance"""
    resp = requests.get(f'{FHIR_BASE}/Location', params=params)
    return resp.json()

@mcp.tool
def create_measure(data: dict) -> Dict[str, Any]:
    """Create a Measure. The Measure FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Measure<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/cohort-measure-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/cv-measure-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/measure-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/proportion-measure-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/publishable-measure-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/ratio-measure-cqfm<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/PublicHealthMeasure"""
    resp = requests.post(f'{FHIR_BASE}/Measure', json=data)
    return resp.json()

@mcp.tool
def get_measure(resource_id: str) -> Dict[str, Any]:
    """Get a Measure by ID. The Measure FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Measure<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/cohort-measure-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/cv-measure-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/measure-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/proportion-measure-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/publishable-measure-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/ratio-measure-cqfm<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/PublicHealthMeasure"""
    resp = requests.get(f'{FHIR_BASE}/Measure/{resource_id}')
    return resp.json()

@mcp.tool
def search_measure(params: dict) -> Dict[str, Any]:
    """Search Measure resources. The Measure FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Measure<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/cohort-measure-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/cv-measure-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/measure-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/proportion-measure-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/publishable-measure-cqfm<br/>Supported profile: http://hl7.org/fhir/us/cqfmeasures/StructureDefinition/ratio-measure-cqfm<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/PublicHealthMeasure"""
    resp = requests.get(f'{FHIR_BASE}/Measure', params=params)
    return resp.json()

@mcp.tool
def create_measurereport(data: dict) -> Dict[str, Any]:
    """Create a MeasureReport. The MeasureReport FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MeasureReport<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/PublicHealthMeasureReport"""
    resp = requests.post(f'{FHIR_BASE}/MeasureReport', json=data)
    return resp.json()

@mcp.tool
def get_measurereport(resource_id: str) -> Dict[str, Any]:
    """Get a MeasureReport by ID. The MeasureReport FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MeasureReport<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/PublicHealthMeasureReport"""
    resp = requests.get(f'{FHIR_BASE}/MeasureReport/{resource_id}')
    return resp.json()

@mcp.tool
def search_measurereport(params: dict) -> Dict[str, Any]:
    """Search MeasureReport resources. The MeasureReport FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MeasureReport<br/>Supported profile: http://hl7.org/fhir/uv/saner/StructureDefinition/PublicHealthMeasureReport"""
    resp = requests.get(f'{FHIR_BASE}/MeasureReport', params=params)
    return resp.json()

@mcp.tool
def create_media(data: dict) -> Dict[str, Any]:
    """Create a Media. The Media FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Media"""
    resp = requests.post(f'{FHIR_BASE}/Media', json=data)
    return resp.json()

@mcp.tool
def get_media(resource_id: str) -> Dict[str, Any]:
    """Get a Media by ID. The Media FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Media"""
    resp = requests.get(f'{FHIR_BASE}/Media/{resource_id}')
    return resp.json()

@mcp.tool
def search_media(params: dict) -> Dict[str, Any]:
    """Search Media resources. The Media FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Media"""
    resp = requests.get(f'{FHIR_BASE}/Media', params=params)
    return resp.json()

@mcp.tool
def create_medication(data: dict) -> Dict[str, Any]:
    """Create a Medication. The Medication FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Medication<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/profile-medication-UVIC1<br/>Supported profile: http://hl7.org/fhir/ca/baseline/StructureDefinition/profile-medication<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-medication<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/Medication-uv-ips<br/>Supported profile: https://fhir.hl7.at/elga-austrianpatientsummary-r4/StructureDefinition/at-aps-medication"""
    resp = requests.post(f'{FHIR_BASE}/Medication', json=data)
    return resp.json()

@mcp.tool
def get_medication(resource_id: str) -> Dict[str, Any]:
    """Get a Medication by ID. The Medication FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Medication<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/profile-medication-UVIC1<br/>Supported profile: http://hl7.org/fhir/ca/baseline/StructureDefinition/profile-medication<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-medication<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/Medication-uv-ips<br/>Supported profile: https://fhir.hl7.at/elga-austrianpatientsummary-r4/StructureDefinition/at-aps-medication"""
    resp = requests.get(f'{FHIR_BASE}/Medication/{resource_id}')
    return resp.json()

@mcp.tool
def search_medication(params: dict) -> Dict[str, Any]:
    """Search Medication resources. The Medication FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Medication<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/profile-medication-UVIC1<br/>Supported profile: http://hl7.org/fhir/ca/baseline/StructureDefinition/profile-medication<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-medication<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/Medication-uv-ips<br/>Supported profile: https://fhir.hl7.at/elga-austrianpatientsummary-r4/StructureDefinition/at-aps-medication"""
    resp = requests.get(f'{FHIR_BASE}/Medication', params=params)
    return resp.json()

@mcp.tool
def create_medicationadministration(data: dict) -> Dict[str, Any]:
    """Create a MedicationAdministration. The MedicationAdministration FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicationAdministration"""
    resp = requests.post(f'{FHIR_BASE}/MedicationAdministration', json=data)
    return resp.json()

@mcp.tool
def get_medicationadministration(resource_id: str) -> Dict[str, Any]:
    """Get a MedicationAdministration by ID. The MedicationAdministration FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicationAdministration"""
    resp = requests.get(f'{FHIR_BASE}/MedicationAdministration/{resource_id}')
    return resp.json()

@mcp.tool
def search_medicationadministration(params: dict) -> Dict[str, Any]:
    """Search MedicationAdministration resources. The MedicationAdministration FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicationAdministration"""
    resp = requests.get(f'{FHIR_BASE}/MedicationAdministration', params=params)
    return resp.json()

@mcp.tool
def create_medicationdispense(data: dict) -> Dict[str, Any]:
    """Create a MedicationDispense. The MedicationDispense FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicationDispense"""
    resp = requests.post(f'{FHIR_BASE}/MedicationDispense', json=data)
    return resp.json()

@mcp.tool
def get_medicationdispense(resource_id: str) -> Dict[str, Any]:
    """Get a MedicationDispense by ID. The MedicationDispense FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicationDispense"""
    resp = requests.get(f'{FHIR_BASE}/MedicationDispense/{resource_id}')
    return resp.json()

@mcp.tool
def search_medicationdispense(params: dict) -> Dict[str, Any]:
    """Search MedicationDispense resources. The MedicationDispense FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicationDispense"""
    resp = requests.get(f'{FHIR_BASE}/MedicationDispense', params=params)
    return resp.json()

@mcp.tool
def create_medicationknowledge(data: dict) -> Dict[str, Any]:
    """Create a MedicationKnowledge. The MedicationKnowledge FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicationKnowledge"""
    resp = requests.post(f'{FHIR_BASE}/MedicationKnowledge', json=data)
    return resp.json()

@mcp.tool
def get_medicationknowledge(resource_id: str) -> Dict[str, Any]:
    """Get a MedicationKnowledge by ID. The MedicationKnowledge FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicationKnowledge"""
    resp = requests.get(f'{FHIR_BASE}/MedicationKnowledge/{resource_id}')
    return resp.json()

@mcp.tool
def search_medicationknowledge(params: dict) -> Dict[str, Any]:
    """Search MedicationKnowledge resources. The MedicationKnowledge FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicationKnowledge"""
    resp = requests.get(f'{FHIR_BASE}/MedicationKnowledge', params=params)
    return resp.json()

@mcp.tool
def create_medicationrequest(data: dict) -> Dict[str, Any]:
    """Create a MedicationRequest. The MedicationRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicationRequest<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-medicationrequest"""
    resp = requests.post(f'{FHIR_BASE}/MedicationRequest', json=data)
    return resp.json()

@mcp.tool
def get_medicationrequest(resource_id: str) -> Dict[str, Any]:
    """Get a MedicationRequest by ID. The MedicationRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicationRequest<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-medicationrequest"""
    resp = requests.get(f'{FHIR_BASE}/MedicationRequest/{resource_id}')
    return resp.json()

@mcp.tool
def search_medicationrequest(params: dict) -> Dict[str, Any]:
    """Search MedicationRequest resources. The MedicationRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicationRequest<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-medicationrequest"""
    resp = requests.get(f'{FHIR_BASE}/MedicationRequest', params=params)
    return resp.json()

@mcp.tool
def create_medicationstatement(data: dict) -> Dict[str, Any]:
    """Create a MedicationStatement. The MedicationStatement FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicationStatement<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/medicationstatement<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/MedicationStatement-uv-ips<br/>Supported profile: https://fhir.hl7.at/elga-austrianpatientsummary-r4/StructureDefinition/at-aps-medicationstatement"""
    resp = requests.post(f'{FHIR_BASE}/MedicationStatement', json=data)
    return resp.json()

@mcp.tool
def get_medicationstatement(resource_id: str) -> Dict[str, Any]:
    """Get a MedicationStatement by ID. The MedicationStatement FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicationStatement<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/medicationstatement<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/MedicationStatement-uv-ips<br/>Supported profile: https://fhir.hl7.at/elga-austrianpatientsummary-r4/StructureDefinition/at-aps-medicationstatement"""
    resp = requests.get(f'{FHIR_BASE}/MedicationStatement/{resource_id}')
    return resp.json()

@mcp.tool
def search_medicationstatement(params: dict) -> Dict[str, Any]:
    """Search MedicationStatement resources. The MedicationStatement FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicationStatement<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/medicationstatement<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/MedicationStatement-uv-ips<br/>Supported profile: https://fhir.hl7.at/elga-austrianpatientsummary-r4/StructureDefinition/at-aps-medicationstatement"""
    resp = requests.get(f'{FHIR_BASE}/MedicationStatement', params=params)
    return resp.json()

@mcp.tool
def create_medicinalproduct(data: dict) -> Dict[str, Any]:
    """Create a MedicinalProduct. The MedicinalProduct FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProduct"""
    resp = requests.post(f'{FHIR_BASE}/MedicinalProduct', json=data)
    return resp.json()

@mcp.tool
def get_medicinalproduct(resource_id: str) -> Dict[str, Any]:
    """Get a MedicinalProduct by ID. The MedicinalProduct FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProduct"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProduct/{resource_id}')
    return resp.json()

@mcp.tool
def search_medicinalproduct(params: dict) -> Dict[str, Any]:
    """Search MedicinalProduct resources. The MedicinalProduct FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProduct"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProduct', params=params)
    return resp.json()

@mcp.tool
def create_medicinalproductauthorization(data: dict) -> Dict[str, Any]:
    """Create a MedicinalProductAuthorization. The MedicinalProductAuthorization FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductAuthorization"""
    resp = requests.post(f'{FHIR_BASE}/MedicinalProductAuthorization', json=data)
    return resp.json()

@mcp.tool
def get_medicinalproductauthorization(resource_id: str) -> Dict[str, Any]:
    """Get a MedicinalProductAuthorization by ID. The MedicinalProductAuthorization FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductAuthorization"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductAuthorization/{resource_id}')
    return resp.json()

@mcp.tool
def search_medicinalproductauthorization(params: dict) -> Dict[str, Any]:
    """Search MedicinalProductAuthorization resources. The MedicinalProductAuthorization FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductAuthorization"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductAuthorization', params=params)
    return resp.json()

@mcp.tool
def create_medicinalproductcontraindication(data: dict) -> Dict[str, Any]:
    """Create a MedicinalProductContraindication. The MedicinalProductContraindication FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductContraindication"""
    resp = requests.post(f'{FHIR_BASE}/MedicinalProductContraindication', json=data)
    return resp.json()

@mcp.tool
def get_medicinalproductcontraindication(resource_id: str) -> Dict[str, Any]:
    """Get a MedicinalProductContraindication by ID. The MedicinalProductContraindication FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductContraindication"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductContraindication/{resource_id}')
    return resp.json()

@mcp.tool
def search_medicinalproductcontraindication(params: dict) -> Dict[str, Any]:
    """Search MedicinalProductContraindication resources. The MedicinalProductContraindication FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductContraindication"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductContraindication', params=params)
    return resp.json()

@mcp.tool
def create_medicinalproductindication(data: dict) -> Dict[str, Any]:
    """Create a MedicinalProductIndication. The MedicinalProductIndication FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductIndication"""
    resp = requests.post(f'{FHIR_BASE}/MedicinalProductIndication', json=data)
    return resp.json()

@mcp.tool
def get_medicinalproductindication(resource_id: str) -> Dict[str, Any]:
    """Get a MedicinalProductIndication by ID. The MedicinalProductIndication FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductIndication"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductIndication/{resource_id}')
    return resp.json()

@mcp.tool
def search_medicinalproductindication(params: dict) -> Dict[str, Any]:
    """Search MedicinalProductIndication resources. The MedicinalProductIndication FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductIndication"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductIndication', params=params)
    return resp.json()

@mcp.tool
def create_medicinalproductingredient(data: dict) -> Dict[str, Any]:
    """Create a MedicinalProductIngredient. The MedicinalProductIngredient FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductIngredient"""
    resp = requests.post(f'{FHIR_BASE}/MedicinalProductIngredient', json=data)
    return resp.json()

@mcp.tool
def get_medicinalproductingredient(resource_id: str) -> Dict[str, Any]:
    """Get a MedicinalProductIngredient by ID. The MedicinalProductIngredient FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductIngredient"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductIngredient/{resource_id}')
    return resp.json()

@mcp.tool
def search_medicinalproductingredient(params: dict) -> Dict[str, Any]:
    """Search MedicinalProductIngredient resources. The MedicinalProductIngredient FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductIngredient"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductIngredient', params=params)
    return resp.json()

@mcp.tool
def create_medicinalproductinteraction(data: dict) -> Dict[str, Any]:
    """Create a MedicinalProductInteraction. The MedicinalProductInteraction FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductInteraction"""
    resp = requests.post(f'{FHIR_BASE}/MedicinalProductInteraction', json=data)
    return resp.json()

@mcp.tool
def get_medicinalproductinteraction(resource_id: str) -> Dict[str, Any]:
    """Get a MedicinalProductInteraction by ID. The MedicinalProductInteraction FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductInteraction"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductInteraction/{resource_id}')
    return resp.json()

@mcp.tool
def search_medicinalproductinteraction(params: dict) -> Dict[str, Any]:
    """Search MedicinalProductInteraction resources. The MedicinalProductInteraction FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductInteraction"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductInteraction', params=params)
    return resp.json()

@mcp.tool
def create_medicinalproductmanufactured(data: dict) -> Dict[str, Any]:
    """Create a MedicinalProductManufactured. The MedicinalProductManufactured FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductManufactured"""
    resp = requests.post(f'{FHIR_BASE}/MedicinalProductManufactured', json=data)
    return resp.json()

@mcp.tool
def get_medicinalproductmanufactured(resource_id: str) -> Dict[str, Any]:
    """Get a MedicinalProductManufactured by ID. The MedicinalProductManufactured FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductManufactured"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductManufactured/{resource_id}')
    return resp.json()

@mcp.tool
def search_medicinalproductmanufactured(params: dict) -> Dict[str, Any]:
    """Search MedicinalProductManufactured resources. The MedicinalProductManufactured FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductManufactured"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductManufactured', params=params)
    return resp.json()

@mcp.tool
def create_medicinalproductpackaged(data: dict) -> Dict[str, Any]:
    """Create a MedicinalProductPackaged. The MedicinalProductPackaged FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductPackaged"""
    resp = requests.post(f'{FHIR_BASE}/MedicinalProductPackaged', json=data)
    return resp.json()

@mcp.tool
def get_medicinalproductpackaged(resource_id: str) -> Dict[str, Any]:
    """Get a MedicinalProductPackaged by ID. The MedicinalProductPackaged FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductPackaged"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductPackaged/{resource_id}')
    return resp.json()

@mcp.tool
def search_medicinalproductpackaged(params: dict) -> Dict[str, Any]:
    """Search MedicinalProductPackaged resources. The MedicinalProductPackaged FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductPackaged"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductPackaged', params=params)
    return resp.json()

@mcp.tool
def create_medicinalproductpharmaceutical(data: dict) -> Dict[str, Any]:
    """Create a MedicinalProductPharmaceutical. The MedicinalProductPharmaceutical FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductPharmaceutical"""
    resp = requests.post(f'{FHIR_BASE}/MedicinalProductPharmaceutical', json=data)
    return resp.json()

@mcp.tool
def get_medicinalproductpharmaceutical(resource_id: str) -> Dict[str, Any]:
    """Get a MedicinalProductPharmaceutical by ID. The MedicinalProductPharmaceutical FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductPharmaceutical"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductPharmaceutical/{resource_id}')
    return resp.json()

@mcp.tool
def search_medicinalproductpharmaceutical(params: dict) -> Dict[str, Any]:
    """Search MedicinalProductPharmaceutical resources. The MedicinalProductPharmaceutical FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductPharmaceutical"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductPharmaceutical', params=params)
    return resp.json()

@mcp.tool
def create_medicinalproductundesirableeffect(data: dict) -> Dict[str, Any]:
    """Create a MedicinalProductUndesirableEffect. The MedicinalProductUndesirableEffect FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductUndesirableEffect"""
    resp = requests.post(f'{FHIR_BASE}/MedicinalProductUndesirableEffect', json=data)
    return resp.json()

@mcp.tool
def get_medicinalproductundesirableeffect(resource_id: str) -> Dict[str, Any]:
    """Get a MedicinalProductUndesirableEffect by ID. The MedicinalProductUndesirableEffect FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductUndesirableEffect"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductUndesirableEffect/{resource_id}')
    return resp.json()

@mcp.tool
def search_medicinalproductundesirableeffect(params: dict) -> Dict[str, Any]:
    """Search MedicinalProductUndesirableEffect resources. The MedicinalProductUndesirableEffect FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductUndesirableEffect"""
    resp = requests.get(f'{FHIR_BASE}/MedicinalProductUndesirableEffect', params=params)
    return resp.json()

@mcp.tool
def create_messagedefinition(data: dict) -> Dict[str, Any]:
    """Create a MessageDefinition. The MessageDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MessageDefinition"""
    resp = requests.post(f'{FHIR_BASE}/MessageDefinition', json=data)
    return resp.json()

@mcp.tool
def get_messagedefinition(resource_id: str) -> Dict[str, Any]:
    """Get a MessageDefinition by ID. The MessageDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MessageDefinition"""
    resp = requests.get(f'{FHIR_BASE}/MessageDefinition/{resource_id}')
    return resp.json()

@mcp.tool
def search_messagedefinition(params: dict) -> Dict[str, Any]:
    """Search MessageDefinition resources. The MessageDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MessageDefinition"""
    resp = requests.get(f'{FHIR_BASE}/MessageDefinition', params=params)
    return resp.json()

@mcp.tool
def create_messageheader(data: dict) -> Dict[str, Any]:
    """Create a MessageHeader. The MessageHeader FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MessageHeader"""
    resp = requests.post(f'{FHIR_BASE}/MessageHeader', json=data)
    return resp.json()

@mcp.tool
def get_messageheader(resource_id: str) -> Dict[str, Any]:
    """Get a MessageHeader by ID. The MessageHeader FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MessageHeader"""
    resp = requests.get(f'{FHIR_BASE}/MessageHeader/{resource_id}')
    return resp.json()

@mcp.tool
def search_messageheader(params: dict) -> Dict[str, Any]:
    """Search MessageHeader resources. The MessageHeader FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MessageHeader"""
    resp = requests.get(f'{FHIR_BASE}/MessageHeader', params=params)
    return resp.json()

@mcp.tool
def create_molecularsequence(data: dict) -> Dict[str, Any]:
    """Create a MolecularSequence. The MolecularSequence FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MolecularSequence"""
    resp = requests.post(f'{FHIR_BASE}/MolecularSequence', json=data)
    return resp.json()

@mcp.tool
def get_molecularsequence(resource_id: str) -> Dict[str, Any]:
    """Get a MolecularSequence by ID. The MolecularSequence FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MolecularSequence"""
    resp = requests.get(f'{FHIR_BASE}/MolecularSequence/{resource_id}')
    return resp.json()

@mcp.tool
def search_molecularsequence(params: dict) -> Dict[str, Any]:
    """Search MolecularSequence resources. The MolecularSequence FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/MolecularSequence"""
    resp = requests.get(f'{FHIR_BASE}/MolecularSequence', params=params)
    return resp.json()

@mcp.tool
def create_namingsystem(data: dict) -> Dict[str, Any]:
    """Create a NamingSystem. The NamingSystem FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/NamingSystem"""
    resp = requests.post(f'{FHIR_BASE}/NamingSystem', json=data)
    return resp.json()

@mcp.tool
def get_namingsystem(resource_id: str) -> Dict[str, Any]:
    """Get a NamingSystem by ID. The NamingSystem FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/NamingSystem"""
    resp = requests.get(f'{FHIR_BASE}/NamingSystem/{resource_id}')
    return resp.json()

@mcp.tool
def search_namingsystem(params: dict) -> Dict[str, Any]:
    """Search NamingSystem resources. The NamingSystem FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/NamingSystem"""
    resp = requests.get(f'{FHIR_BASE}/NamingSystem', params=params)
    return resp.json()

@mcp.tool
def create_nutritionorder(data: dict) -> Dict[str, Any]:
    """Create a NutritionOrder. The NutritionOrder FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/NutritionOrder"""
    resp = requests.post(f'{FHIR_BASE}/NutritionOrder', json=data)
    return resp.json()

@mcp.tool
def get_nutritionorder(resource_id: str) -> Dict[str, Any]:
    """Get a NutritionOrder by ID. The NutritionOrder FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/NutritionOrder"""
    resp = requests.get(f'{FHIR_BASE}/NutritionOrder/{resource_id}')
    return resp.json()

@mcp.tool
def search_nutritionorder(params: dict) -> Dict[str, Any]:
    """Search NutritionOrder resources. The NutritionOrder FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/NutritionOrder"""
    resp = requests.get(f'{FHIR_BASE}/NutritionOrder', params=params)
    return resp.json()

@mcp.tool
def create_observation(data: dict) -> Dict[str, Any]:
    """Create a Observation. The Observation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Observation<br/>Supported profile: http://example.org/fhir/StructureDefinition/MyObservation<br/>Supported profile: http://example.org/fhir/StructureDefinition/ShObservation<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/619087<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/98765432<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/BloodPressure1<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/HRV-POC-1<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/bp<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/resprate<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/vitalsigns<br/>Supported profile: http://hl7.org/fhir/us/PACIO-functional-cognitive-status/StructureDefinition/pacio-cs-BundledCognitiveStatus<br/>Supported profile: http://hl7.org/fhir/us/PACIO-functional-cognitive-status/StructureDefinition/pacio-cs-CognitiveStatus<br/>Supported profile: http://hl7.org/fhir/us/PACIO-functional-cognitive-status/StructureDefinition/pacio-fs-BundledFunctionalStatus<br/>Supported profile: http://hl7.org/fhir/us/PACIO-functional-cognitive-status/StructureDefinition/pacio-fs-FunctionalStatus<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Observation-characteristic-of-labor-and-delivery<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Observation-mother-received-wic-food<br/>Supported profile: http://hl7.org/fhir/us/birthdefectreporting/StructureDefinition/observation-mother-drug-use<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/pediatric-bmi-for-age<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/pediatric-weight-for-height<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-pulse-oximetry<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-smokingstatus<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/diagnostic-implication<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/finding<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/genomics-base<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/genotype<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/grouper<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/haplotype<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/implication<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/msi<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/overall-interpretation<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/region-studied<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/sequence-phase-relationship<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/therapeutic-implication<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/tmb<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/variant<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/Observation-results-laboratory-uv-ips<br/>Supported profile: http://hl7.org/fhir/uv/smarthealthcards-vaccination/StructureDefinition/covid19-laboratory-result-observation<br/>Supported profile: http://phr.kanta.fi/StructureDefinition/fiphr-sd-moderatetovigorouspatime<br/>Supported profile: http://phr.kanta.fi/StructureDefinition/fiphr-sd-spirometryresult-test<br/>Supported profile: https://hapi.fhir.org/baseR4/StructureDefinition/1256483<br/>Supported profile: https://hapi.fhir.org/baseR4/StructureDefinition/HRV-POC-1<br/>Supported profile: https://hapi.fhir.org/baseR4/StructureDefinition/ShObservation<br/>Supported profile: https://trifolia-fhir-dev.lantanagroup.com/observation-display-test<br/>Supported profile: https://www.fhir.philips.com/4.0/StructureDefinition/common/core/vitalSign-v1/BloodPressureVitalSign"""
    resp = requests.post(f'{FHIR_BASE}/Observation', json=data)
    return resp.json()

@mcp.tool
def get_observation(resource_id: str) -> Dict[str, Any]:
    """Get a Observation by ID. The Observation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Observation<br/>Supported profile: http://example.org/fhir/StructureDefinition/MyObservation<br/>Supported profile: http://example.org/fhir/StructureDefinition/ShObservation<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/619087<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/98765432<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/BloodPressure1<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/HRV-POC-1<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/bp<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/resprate<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/vitalsigns<br/>Supported profile: http://hl7.org/fhir/us/PACIO-functional-cognitive-status/StructureDefinition/pacio-cs-BundledCognitiveStatus<br/>Supported profile: http://hl7.org/fhir/us/PACIO-functional-cognitive-status/StructureDefinition/pacio-cs-CognitiveStatus<br/>Supported profile: http://hl7.org/fhir/us/PACIO-functional-cognitive-status/StructureDefinition/pacio-fs-BundledFunctionalStatus<br/>Supported profile: http://hl7.org/fhir/us/PACIO-functional-cognitive-status/StructureDefinition/pacio-fs-FunctionalStatus<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Observation-characteristic-of-labor-and-delivery<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Observation-mother-received-wic-food<br/>Supported profile: http://hl7.org/fhir/us/birthdefectreporting/StructureDefinition/observation-mother-drug-use<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/pediatric-bmi-for-age<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/pediatric-weight-for-height<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-pulse-oximetry<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-smokingstatus<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/diagnostic-implication<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/finding<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/genomics-base<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/genotype<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/grouper<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/haplotype<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/implication<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/msi<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/overall-interpretation<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/region-studied<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/sequence-phase-relationship<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/therapeutic-implication<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/tmb<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/variant<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/Observation-results-laboratory-uv-ips<br/>Supported profile: http://hl7.org/fhir/uv/smarthealthcards-vaccination/StructureDefinition/covid19-laboratory-result-observation<br/>Supported profile: http://phr.kanta.fi/StructureDefinition/fiphr-sd-moderatetovigorouspatime<br/>Supported profile: http://phr.kanta.fi/StructureDefinition/fiphr-sd-spirometryresult-test<br/>Supported profile: https://hapi.fhir.org/baseR4/StructureDefinition/1256483<br/>Supported profile: https://hapi.fhir.org/baseR4/StructureDefinition/HRV-POC-1<br/>Supported profile: https://hapi.fhir.org/baseR4/StructureDefinition/ShObservation<br/>Supported profile: https://trifolia-fhir-dev.lantanagroup.com/observation-display-test<br/>Supported profile: https://www.fhir.philips.com/4.0/StructureDefinition/common/core/vitalSign-v1/BloodPressureVitalSign"""
    resp = requests.get(f'{FHIR_BASE}/Observation/{resource_id}')
    return resp.json()

@mcp.tool
def search_observation(params: dict) -> Dict[str, Any]:
    """Search Observation resources. The Observation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Observation<br/>Supported profile: http://example.org/fhir/StructureDefinition/MyObservation<br/>Supported profile: http://example.org/fhir/StructureDefinition/ShObservation<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/619087<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/98765432<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/BloodPressure1<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/HRV-POC-1<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/bp<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/resprate<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/vitalsigns<br/>Supported profile: http://hl7.org/fhir/us/PACIO-functional-cognitive-status/StructureDefinition/pacio-cs-BundledCognitiveStatus<br/>Supported profile: http://hl7.org/fhir/us/PACIO-functional-cognitive-status/StructureDefinition/pacio-cs-CognitiveStatus<br/>Supported profile: http://hl7.org/fhir/us/PACIO-functional-cognitive-status/StructureDefinition/pacio-fs-BundledFunctionalStatus<br/>Supported profile: http://hl7.org/fhir/us/PACIO-functional-cognitive-status/StructureDefinition/pacio-fs-FunctionalStatus<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Observation-characteristic-of-labor-and-delivery<br/>Supported profile: http://hl7.org/fhir/us/bfdr/StructureDefinition/Observation-mother-received-wic-food<br/>Supported profile: http://hl7.org/fhir/us/birthdefectreporting/StructureDefinition/observation-mother-drug-use<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/pediatric-bmi-for-age<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/pediatric-weight-for-height<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-pulse-oximetry<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-smokingstatus<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/diagnostic-implication<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/finding<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/genomics-base<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/genotype<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/grouper<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/haplotype<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/implication<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/msi<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/overall-interpretation<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/region-studied<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/sequence-phase-relationship<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/therapeutic-implication<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/tmb<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/variant<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/Observation-results-laboratory-uv-ips<br/>Supported profile: http://hl7.org/fhir/uv/smarthealthcards-vaccination/StructureDefinition/covid19-laboratory-result-observation<br/>Supported profile: http://phr.kanta.fi/StructureDefinition/fiphr-sd-moderatetovigorouspatime<br/>Supported profile: http://phr.kanta.fi/StructureDefinition/fiphr-sd-spirometryresult-test<br/>Supported profile: https://hapi.fhir.org/baseR4/StructureDefinition/1256483<br/>Supported profile: https://hapi.fhir.org/baseR4/StructureDefinition/HRV-POC-1<br/>Supported profile: https://hapi.fhir.org/baseR4/StructureDefinition/ShObservation<br/>Supported profile: https://trifolia-fhir-dev.lantanagroup.com/observation-display-test<br/>Supported profile: https://www.fhir.philips.com/4.0/StructureDefinition/common/core/vitalSign-v1/BloodPressureVitalSign"""
    resp = requests.get(f'{FHIR_BASE}/Observation', params=params)
    return resp.json()

@mcp.tool
def create_observationdefinition(data: dict) -> Dict[str, Any]:
    """Create a ObservationDefinition. The ObservationDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ObservationDefinition"""
    resp = requests.post(f'{FHIR_BASE}/ObservationDefinition', json=data)
    return resp.json()

@mcp.tool
def get_observationdefinition(resource_id: str) -> Dict[str, Any]:
    """Get a ObservationDefinition by ID. The ObservationDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ObservationDefinition"""
    resp = requests.get(f'{FHIR_BASE}/ObservationDefinition/{resource_id}')
    return resp.json()

@mcp.tool
def search_observationdefinition(params: dict) -> Dict[str, Any]:
    """Search ObservationDefinition resources. The ObservationDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ObservationDefinition"""
    resp = requests.get(f'{FHIR_BASE}/ObservationDefinition', params=params)
    return resp.json()

@mcp.tool
def create_operationdefinition(data: dict) -> Dict[str, Any]:
    """Create a OperationDefinition. The OperationDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition"""
    resp = requests.post(f'{FHIR_BASE}/OperationDefinition', json=data)
    return resp.json()

@mcp.tool
def get_operationdefinition(resource_id: str) -> Dict[str, Any]:
    """Get a OperationDefinition by ID. The OperationDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition"""
    resp = requests.get(f'{FHIR_BASE}/OperationDefinition/{resource_id}')
    return resp.json()

@mcp.tool
def search_operationdefinition(params: dict) -> Dict[str, Any]:
    """Search OperationDefinition resources. The OperationDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/OperationDefinition"""
    resp = requests.get(f'{FHIR_BASE}/OperationDefinition', params=params)
    return resp.json()

@mcp.tool
def create_operationoutcome(data: dict) -> Dict[str, Any]:
    """Create a OperationOutcome. The OperationOutcome FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/OperationOutcome"""
    resp = requests.post(f'{FHIR_BASE}/OperationOutcome', json=data)
    return resp.json()

@mcp.tool
def get_operationoutcome(resource_id: str) -> Dict[str, Any]:
    """Get a OperationOutcome by ID. The OperationOutcome FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/OperationOutcome"""
    resp = requests.get(f'{FHIR_BASE}/OperationOutcome/{resource_id}')
    return resp.json()

@mcp.tool
def search_operationoutcome(params: dict) -> Dict[str, Any]:
    """Search OperationOutcome resources. The OperationOutcome FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/OperationOutcome"""
    resp = requests.get(f'{FHIR_BASE}/OperationOutcome', params=params)
    return resp.json()

@mcp.tool
def create_organization(data: dict) -> Dict[str, Any]:
    """Create a Organization. The Organization FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Organization<br/>Supported profile: http://fhir.nl/fhir/StructureDefinition/nl-core-organization<br/>Supported profile: http://hl7.alp/StructureDefinition/AlpCoreOrganization<br/>Supported profile: http://hl7.org.nz/fhir/StructureDefinition/HpiOrganization<br/>Supported profile: http://hl7.org.nz/fhir/healthAlliance/StructureDefinition/HaOrganization<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization<br/>Supported profile: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization<br/>Supported profile: https://fhir.kbv.de/StructureDefinition/74_PR_VoS_Betriebsstaette<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.FacilityOrganization<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.JurisdictionOrganization<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.Organization<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-organization"""
    resp = requests.post(f'{FHIR_BASE}/Organization', json=data)
    return resp.json()

@mcp.tool
def get_organization(resource_id: str) -> Dict[str, Any]:
    """Get a Organization by ID. The Organization FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Organization<br/>Supported profile: http://fhir.nl/fhir/StructureDefinition/nl-core-organization<br/>Supported profile: http://hl7.alp/StructureDefinition/AlpCoreOrganization<br/>Supported profile: http://hl7.org.nz/fhir/StructureDefinition/HpiOrganization<br/>Supported profile: http://hl7.org.nz/fhir/healthAlliance/StructureDefinition/HaOrganization<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization<br/>Supported profile: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization<br/>Supported profile: https://fhir.kbv.de/StructureDefinition/74_PR_VoS_Betriebsstaette<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.FacilityOrganization<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.JurisdictionOrganization<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.Organization<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-organization"""
    resp = requests.get(f'{FHIR_BASE}/Organization/{resource_id}')
    return resp.json()

@mcp.tool
def search_organization(params: dict) -> Dict[str, Any]:
    """Search Organization resources. The Organization FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Organization<br/>Supported profile: http://fhir.nl/fhir/StructureDefinition/nl-core-organization<br/>Supported profile: http://hl7.alp/StructureDefinition/AlpCoreOrganization<br/>Supported profile: http://hl7.org.nz/fhir/StructureDefinition/HpiOrganization<br/>Supported profile: http://hl7.org.nz/fhir/healthAlliance/StructureDefinition/HaOrganization<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization<br/>Supported profile: http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization<br/>Supported profile: https://fhir.kbv.de/StructureDefinition/74_PR_VoS_Betriebsstaette<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.FacilityOrganization<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.JurisdictionOrganization<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.Organization<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-organization"""
    resp = requests.get(f'{FHIR_BASE}/Organization', params=params)
    return resp.json()

@mcp.tool
def create_organizationaffiliation(data: dict) -> Dict[str, Any]:
    """Create a OrganizationAffiliation. The OrganizationAffiliation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/OrganizationAffiliation"""
    resp = requests.post(f'{FHIR_BASE}/OrganizationAffiliation', json=data)
    return resp.json()

@mcp.tool
def get_organizationaffiliation(resource_id: str) -> Dict[str, Any]:
    """Get a OrganizationAffiliation by ID. The OrganizationAffiliation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/OrganizationAffiliation"""
    resp = requests.get(f'{FHIR_BASE}/OrganizationAffiliation/{resource_id}')
    return resp.json()

@mcp.tool
def search_organizationaffiliation(params: dict) -> Dict[str, Any]:
    """Search OrganizationAffiliation resources. The OrganizationAffiliation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/OrganizationAffiliation"""
    resp = requests.get(f'{FHIR_BASE}/OrganizationAffiliation', params=params)
    return resp.json()

@mcp.tool
def create_parameters(data: dict) -> Dict[str, Any]:
    """Create a Parameters. The Parameters FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Parameters<br/>Supported profile: http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-subscription-status<br/>Supported profile: http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-subscription-topic-canonical-urls"""
    resp = requests.post(f'{FHIR_BASE}/Parameters', json=data)
    return resp.json()

@mcp.tool
def get_parameters(resource_id: str) -> Dict[str, Any]:
    """Get a Parameters by ID. The Parameters FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Parameters<br/>Supported profile: http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-subscription-status<br/>Supported profile: http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-subscription-topic-canonical-urls"""
    resp = requests.get(f'{FHIR_BASE}/Parameters/{resource_id}')
    return resp.json()

@mcp.tool
def search_parameters(params: dict) -> Dict[str, Any]:
    """Search Parameters resources. The Parameters FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Parameters<br/>Supported profile: http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-subscription-status<br/>Supported profile: http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-subscription-topic-canonical-urls"""
    resp = requests.get(f'{FHIR_BASE}/Parameters', params=params)
    return resp.json()

@mcp.tool
def create_patient(data: dict) -> Dict[str, Any]:
    """Create a Patient. The Patient FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Patient<br/>Supported profile: http://berzerkistan.gov.bz/fhir/StructureDefinition/berzerkistanpatient<br/>Supported profile: http://curizent.com/fhir/StructureDefinition/BuildPatientResourceProfile<br/>Supported profile: http://example.gevko.de/fhir/schulung/StructureDefinition/VerfallPatient<br/>Supported profile: http://example.gevko.de/fhir/schulung/StructureDefinition/meinPatient<br/>Supported profile: http://example.org/fhir/StructureDefinition/BMOPatient<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatAnna<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot2<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot3<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot4<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot5<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot6<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot7<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot8<br/>Supported profile: http://example.org/fhir/StructureDefinition/HL7ATBerzekistanPatient<br/>Supported profile: http://example.org/fhir/StructureDefinition/MyPatient1188<br/>Supported profile: http://example.org/fhir/StructureDefinition/Patient_Exercise1<br/>Supported profile: http://example.org/fhir/StructureDefinition/ShPatient<br/>Supported profile: http://example.org/fhir/StructureDefinition/ShPatient11<br/>Supported profile: http://example.org/fhir/StructureDefinition/ShPatient12<br/>Supported profile: http://example.org/fhir/StructureDefinition/ShPatient13<br/>Supported profile: http://example.org/fhir/StructureDefinition/TestAnns2<br/>Supported profile: http://example.org/fhir/StructureDefinition/TestAnns3<br/>Supported profile: http://example.org/fhir/StructureDefinition/TestAnns5<br/>Supported profile: http://example.org/fhir/StructureDefinition/TestPatient_MA<br/>Supported profile: http://example.org/fhir/StructureDefinition/wakanda-core-patient<br/>Supported profile: http://example.org/fhir/fish/StructureDefinition/fish-patient<br/>Supported profile: http://fhir.health.org.il/StructureDefinition/il-core-patient<br/>Supported profile: http://fhir.kids-first.io/StructureDefinition/MyPatchild2<br/>Supported profile: http://fhir.nl/fhir/StructureDefinition/nl-core-patient<br/>Supported profile: http://fhir.org/guides/who/svc-rc1/StructureDefinition/svc-patient<br/>Supported profile: http://hapi.fhir.org//fhir/StructureDefinition/MyPatient04202020A<br/>Supported profile: http://hapi.fhir.org//fhir/StructureDefinition/SidProfile<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/DemoPatient<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/FirstPatientProfileJohn<br/>Supported profile: http://hapi.fhir.org/fhir/StructureDefinition/MyPatientRehan<br/>Supported profile: http://hapi.fhir.org/fhir/StructureDefinition/SidProfile<br/>Supported profile: http://hapi.fhir.org/fhir/StructureDefinition/SidProfile/1<br/>Supported profile: http://hl7.no/fhir/StructureDefinition/no-basis-Patient<br/>Supported profile: http://hl7.org.au/fhir/StructureDefinition/au-patient<br/>Supported profile: http://hl7.org.nz/fhir/healthAlliance/StructureDefinition/HaPatient<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/BMOPatient<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/BMOPatientAnna1<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/custom-Patient-v1<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/custom-Patient-v2<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/Patient-uv-ips<br/>Supported profile: http://hl7.org/fhir123/StructureDefinition/Patient-ibec-CodeSystem<br/>Supported profile: http://jpfhir.jp/fhir/StructureDefinition/JP_Patient<br/>Supported profile: http://jpfhir.jp/fhir/StructureDefinition/JP_Patient|0.0.1<br/>Supported profile: http://jpfhir.jp/fhir/StructureDefinition/JP_Patient|0.0.2<br/>Supported profile: http://jpfhir.jp/fhir/StructureDefinition/JP_Patient|0.8<br/>Supported profile: http://openhie.org/fhir/training-solution-1/StructureDefinition/hiv-patient<br/>Supported profile: https://aehrc.com/fhir/StructureDefinition/AUPrimaryCarePatient<br/>Supported profile: https://corhealth-ontario.ca/fhir/StructureDefinition/corhealth-patient<br/>Supported profile: https://gematik.de/fhir/ISiK/StructureDefinition/ISiKPatient<br/>Supported profile: https://gematik.de/fhir/isik/v2/Basismodul/StructureDefinition/ISiKPatient<br/>Supported profile: https://hapi.fhir.org/baseR4/StructureDefinition/ShPatient<br/>Supported profile: https://jembi.github.io/covid19-immunization-ig//StructureDefinition/covid19-patient<br/>Supported profile: https://nrces.in/ndhm/fhir/r4/StructureDefinition/Patient<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-patient"""
    resp = requests.post(f'{FHIR_BASE}/Patient', json=data)
    return resp.json()

@mcp.tool
def get_patient(resource_id: str) -> Dict[str, Any]:
    """Get a Patient by ID. The Patient FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Patient<br/>Supported profile: http://berzerkistan.gov.bz/fhir/StructureDefinition/berzerkistanpatient<br/>Supported profile: http://curizent.com/fhir/StructureDefinition/BuildPatientResourceProfile<br/>Supported profile: http://example.gevko.de/fhir/schulung/StructureDefinition/VerfallPatient<br/>Supported profile: http://example.gevko.de/fhir/schulung/StructureDefinition/meinPatient<br/>Supported profile: http://example.org/fhir/StructureDefinition/BMOPatient<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatAnna<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot2<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot3<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot4<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot5<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot6<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot7<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot8<br/>Supported profile: http://example.org/fhir/StructureDefinition/HL7ATBerzekistanPatient<br/>Supported profile: http://example.org/fhir/StructureDefinition/MyPatient1188<br/>Supported profile: http://example.org/fhir/StructureDefinition/Patient_Exercise1<br/>Supported profile: http://example.org/fhir/StructureDefinition/ShPatient<br/>Supported profile: http://example.org/fhir/StructureDefinition/ShPatient11<br/>Supported profile: http://example.org/fhir/StructureDefinition/ShPatient12<br/>Supported profile: http://example.org/fhir/StructureDefinition/ShPatient13<br/>Supported profile: http://example.org/fhir/StructureDefinition/TestAnns2<br/>Supported profile: http://example.org/fhir/StructureDefinition/TestAnns3<br/>Supported profile: http://example.org/fhir/StructureDefinition/TestAnns5<br/>Supported profile: http://example.org/fhir/StructureDefinition/TestPatient_MA<br/>Supported profile: http://example.org/fhir/StructureDefinition/wakanda-core-patient<br/>Supported profile: http://example.org/fhir/fish/StructureDefinition/fish-patient<br/>Supported profile: http://fhir.health.org.il/StructureDefinition/il-core-patient<br/>Supported profile: http://fhir.kids-first.io/StructureDefinition/MyPatchild2<br/>Supported profile: http://fhir.nl/fhir/StructureDefinition/nl-core-patient<br/>Supported profile: http://fhir.org/guides/who/svc-rc1/StructureDefinition/svc-patient<br/>Supported profile: http://hapi.fhir.org//fhir/StructureDefinition/MyPatient04202020A<br/>Supported profile: http://hapi.fhir.org//fhir/StructureDefinition/SidProfile<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/DemoPatient<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/FirstPatientProfileJohn<br/>Supported profile: http://hapi.fhir.org/fhir/StructureDefinition/MyPatientRehan<br/>Supported profile: http://hapi.fhir.org/fhir/StructureDefinition/SidProfile<br/>Supported profile: http://hapi.fhir.org/fhir/StructureDefinition/SidProfile/1<br/>Supported profile: http://hl7.no/fhir/StructureDefinition/no-basis-Patient<br/>Supported profile: http://hl7.org.au/fhir/StructureDefinition/au-patient<br/>Supported profile: http://hl7.org.nz/fhir/healthAlliance/StructureDefinition/HaPatient<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/BMOPatient<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/BMOPatientAnna1<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/custom-Patient-v1<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/custom-Patient-v2<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/Patient-uv-ips<br/>Supported profile: http://hl7.org/fhir123/StructureDefinition/Patient-ibec-CodeSystem<br/>Supported profile: http://jpfhir.jp/fhir/StructureDefinition/JP_Patient<br/>Supported profile: http://jpfhir.jp/fhir/StructureDefinition/JP_Patient|0.0.1<br/>Supported profile: http://jpfhir.jp/fhir/StructureDefinition/JP_Patient|0.0.2<br/>Supported profile: http://jpfhir.jp/fhir/StructureDefinition/JP_Patient|0.8<br/>Supported profile: http://openhie.org/fhir/training-solution-1/StructureDefinition/hiv-patient<br/>Supported profile: https://aehrc.com/fhir/StructureDefinition/AUPrimaryCarePatient<br/>Supported profile: https://corhealth-ontario.ca/fhir/StructureDefinition/corhealth-patient<br/>Supported profile: https://gematik.de/fhir/ISiK/StructureDefinition/ISiKPatient<br/>Supported profile: https://gematik.de/fhir/isik/v2/Basismodul/StructureDefinition/ISiKPatient<br/>Supported profile: https://hapi.fhir.org/baseR4/StructureDefinition/ShPatient<br/>Supported profile: https://jembi.github.io/covid19-immunization-ig//StructureDefinition/covid19-patient<br/>Supported profile: https://nrces.in/ndhm/fhir/r4/StructureDefinition/Patient<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-patient"""
    resp = requests.get(f'{FHIR_BASE}/Patient/{resource_id}')
    return resp.json()

@mcp.tool
def search_patient(params: dict) -> Dict[str, Any]:
    """Search Patient resources. The Patient FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Patient<br/>Supported profile: http://berzerkistan.gov.bz/fhir/StructureDefinition/berzerkistanpatient<br/>Supported profile: http://curizent.com/fhir/StructureDefinition/BuildPatientResourceProfile<br/>Supported profile: http://example.gevko.de/fhir/schulung/StructureDefinition/VerfallPatient<br/>Supported profile: http://example.gevko.de/fhir/schulung/StructureDefinition/meinPatient<br/>Supported profile: http://example.org/fhir/StructureDefinition/BMOPatient<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatAnna<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot2<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot3<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot4<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot5<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot6<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot7<br/>Supported profile: http://example.org/fhir/StructureDefinition/BezPatSnapshot8<br/>Supported profile: http://example.org/fhir/StructureDefinition/HL7ATBerzekistanPatient<br/>Supported profile: http://example.org/fhir/StructureDefinition/MyPatient1188<br/>Supported profile: http://example.org/fhir/StructureDefinition/Patient_Exercise1<br/>Supported profile: http://example.org/fhir/StructureDefinition/ShPatient<br/>Supported profile: http://example.org/fhir/StructureDefinition/ShPatient11<br/>Supported profile: http://example.org/fhir/StructureDefinition/ShPatient12<br/>Supported profile: http://example.org/fhir/StructureDefinition/ShPatient13<br/>Supported profile: http://example.org/fhir/StructureDefinition/TestAnns2<br/>Supported profile: http://example.org/fhir/StructureDefinition/TestAnns3<br/>Supported profile: http://example.org/fhir/StructureDefinition/TestAnns5<br/>Supported profile: http://example.org/fhir/StructureDefinition/TestPatient_MA<br/>Supported profile: http://example.org/fhir/StructureDefinition/wakanda-core-patient<br/>Supported profile: http://example.org/fhir/fish/StructureDefinition/fish-patient<br/>Supported profile: http://fhir.health.org.il/StructureDefinition/il-core-patient<br/>Supported profile: http://fhir.kids-first.io/StructureDefinition/MyPatchild2<br/>Supported profile: http://fhir.nl/fhir/StructureDefinition/nl-core-patient<br/>Supported profile: http://fhir.org/guides/who/svc-rc1/StructureDefinition/svc-patient<br/>Supported profile: http://hapi.fhir.org//fhir/StructureDefinition/MyPatient04202020A<br/>Supported profile: http://hapi.fhir.org//fhir/StructureDefinition/SidProfile<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/DemoPatient<br/>Supported profile: http://hapi.fhir.org/baseR4/StructureDefinition/FirstPatientProfileJohn<br/>Supported profile: http://hapi.fhir.org/fhir/StructureDefinition/MyPatientRehan<br/>Supported profile: http://hapi.fhir.org/fhir/StructureDefinition/SidProfile<br/>Supported profile: http://hapi.fhir.org/fhir/StructureDefinition/SidProfile/1<br/>Supported profile: http://hl7.no/fhir/StructureDefinition/no-basis-Patient<br/>Supported profile: http://hl7.org.au/fhir/StructureDefinition/au-patient<br/>Supported profile: http://hl7.org.nz/fhir/healthAlliance/StructureDefinition/HaPatient<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/BMOPatient<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/BMOPatientAnna1<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/custom-Patient-v1<br/>Supported profile: http://hl7.org/fhir/StructureDefinition/custom-Patient-v2<br/>Supported profile: http://hl7.org/fhir/uv/ips/StructureDefinition/Patient-uv-ips<br/>Supported profile: http://hl7.org/fhir123/StructureDefinition/Patient-ibec-CodeSystem<br/>Supported profile: http://jpfhir.jp/fhir/StructureDefinition/JP_Patient<br/>Supported profile: http://jpfhir.jp/fhir/StructureDefinition/JP_Patient|0.0.1<br/>Supported profile: http://jpfhir.jp/fhir/StructureDefinition/JP_Patient|0.0.2<br/>Supported profile: http://jpfhir.jp/fhir/StructureDefinition/JP_Patient|0.8<br/>Supported profile: http://openhie.org/fhir/training-solution-1/StructureDefinition/hiv-patient<br/>Supported profile: https://aehrc.com/fhir/StructureDefinition/AUPrimaryCarePatient<br/>Supported profile: https://corhealth-ontario.ca/fhir/StructureDefinition/corhealth-patient<br/>Supported profile: https://gematik.de/fhir/ISiK/StructureDefinition/ISiKPatient<br/>Supported profile: https://gematik.de/fhir/isik/v2/Basismodul/StructureDefinition/ISiKPatient<br/>Supported profile: https://hapi.fhir.org/baseR4/StructureDefinition/ShPatient<br/>Supported profile: https://jembi.github.io/covid19-immunization-ig//StructureDefinition/covid19-patient<br/>Supported profile: https://nrces.in/ndhm/fhir/r4/StructureDefinition/Patient<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-patient"""
    resp = requests.get(f'{FHIR_BASE}/Patient', params=params)
    return resp.json()

@mcp.tool
def create_paymentnotice(data: dict) -> Dict[str, Any]:
    """Create a PaymentNotice. The PaymentNotice FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/PaymentNotice"""
    resp = requests.post(f'{FHIR_BASE}/PaymentNotice', json=data)
    return resp.json()

@mcp.tool
def get_paymentnotice(resource_id: str) -> Dict[str, Any]:
    """Get a PaymentNotice by ID. The PaymentNotice FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/PaymentNotice"""
    resp = requests.get(f'{FHIR_BASE}/PaymentNotice/{resource_id}')
    return resp.json()

@mcp.tool
def search_paymentnotice(params: dict) -> Dict[str, Any]:
    """Search PaymentNotice resources. The PaymentNotice FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/PaymentNotice"""
    resp = requests.get(f'{FHIR_BASE}/PaymentNotice', params=params)
    return resp.json()

@mcp.tool
def create_paymentreconciliation(data: dict) -> Dict[str, Any]:
    """Create a PaymentReconciliation. The PaymentReconciliation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/PaymentReconciliation"""
    resp = requests.post(f'{FHIR_BASE}/PaymentReconciliation', json=data)
    return resp.json()

@mcp.tool
def get_paymentreconciliation(resource_id: str) -> Dict[str, Any]:
    """Get a PaymentReconciliation by ID. The PaymentReconciliation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/PaymentReconciliation"""
    resp = requests.get(f'{FHIR_BASE}/PaymentReconciliation/{resource_id}')
    return resp.json()

@mcp.tool
def search_paymentreconciliation(params: dict) -> Dict[str, Any]:
    """Search PaymentReconciliation resources. The PaymentReconciliation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/PaymentReconciliation"""
    resp = requests.get(f'{FHIR_BASE}/PaymentReconciliation', params=params)
    return resp.json()

@mcp.tool
def create_person(data: dict) -> Dict[str, Any]:
    """Create a Person. The Person FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Person<br/>Supported profile: http://hl7.no/fhir/StructureDefinition/no-basis-Person"""
    resp = requests.post(f'{FHIR_BASE}/Person', json=data)
    return resp.json()

@mcp.tool
def get_person(resource_id: str) -> Dict[str, Any]:
    """Get a Person by ID. The Person FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Person<br/>Supported profile: http://hl7.no/fhir/StructureDefinition/no-basis-Person"""
    resp = requests.get(f'{FHIR_BASE}/Person/{resource_id}')
    return resp.json()

@mcp.tool
def search_person(params: dict) -> Dict[str, Any]:
    """Search Person resources. The Person FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Person<br/>Supported profile: http://hl7.no/fhir/StructureDefinition/no-basis-Person"""
    resp = requests.get(f'{FHIR_BASE}/Person', params=params)
    return resp.json()

@mcp.tool
def create_plandefinition(data: dict) -> Dict[str, Any]:
    """Create a PlanDefinition. The PlanDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/PlanDefinition<br/>Supported profile: http://fkcfhir.org/fhir/StructureDefinition/DialysisServiceDefinition<br/>Supported profile: http://fkcfhir.org/fhir/StructureDefinition/MedicationServiceDefinition<br/>Supported profile: http://hl7.org.nz/fhir/StructureDefinition/CcaPlanDefinition"""
    resp = requests.post(f'{FHIR_BASE}/PlanDefinition', json=data)
    return resp.json()

@mcp.tool
def get_plandefinition(resource_id: str) -> Dict[str, Any]:
    """Get a PlanDefinition by ID. The PlanDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/PlanDefinition<br/>Supported profile: http://fkcfhir.org/fhir/StructureDefinition/DialysisServiceDefinition<br/>Supported profile: http://fkcfhir.org/fhir/StructureDefinition/MedicationServiceDefinition<br/>Supported profile: http://hl7.org.nz/fhir/StructureDefinition/CcaPlanDefinition"""
    resp = requests.get(f'{FHIR_BASE}/PlanDefinition/{resource_id}')
    return resp.json()

@mcp.tool
def search_plandefinition(params: dict) -> Dict[str, Any]:
    """Search PlanDefinition resources. The PlanDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/PlanDefinition<br/>Supported profile: http://fkcfhir.org/fhir/StructureDefinition/DialysisServiceDefinition<br/>Supported profile: http://fkcfhir.org/fhir/StructureDefinition/MedicationServiceDefinition<br/>Supported profile: http://hl7.org.nz/fhir/StructureDefinition/CcaPlanDefinition"""
    resp = requests.get(f'{FHIR_BASE}/PlanDefinition', params=params)
    return resp.json()

@mcp.tool
def create_practitioner(data: dict) -> Dict[str, Any]:
    """Create a Practitioner. The Practitioner FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Practitioner<br/>Supported profile: http://hl7.org.nz/fhir/healthAlliance/StructureDefinition/HaPractitioner<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner<br/>Supported profile: http://interopsante.org/fhir/structuredefinition/resource/fr-practitioner<br/>Supported profile: http://medcom.dk/fhir/xds-poc/StructureDefinition/AuthorPractitioner<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.Practitioner<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-practitioner"""
    resp = requests.post(f'{FHIR_BASE}/Practitioner', json=data)
    return resp.json()

@mcp.tool
def get_practitioner(resource_id: str) -> Dict[str, Any]:
    """Get a Practitioner by ID. The Practitioner FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Practitioner<br/>Supported profile: http://hl7.org.nz/fhir/healthAlliance/StructureDefinition/HaPractitioner<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner<br/>Supported profile: http://interopsante.org/fhir/structuredefinition/resource/fr-practitioner<br/>Supported profile: http://medcom.dk/fhir/xds-poc/StructureDefinition/AuthorPractitioner<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.Practitioner<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-practitioner"""
    resp = requests.get(f'{FHIR_BASE}/Practitioner/{resource_id}')
    return resp.json()

@mcp.tool
def search_practitioner(params: dict) -> Dict[str, Any]:
    """Search Practitioner resources. The Practitioner FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Practitioner<br/>Supported profile: http://hl7.org.nz/fhir/healthAlliance/StructureDefinition/HaPractitioner<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner<br/>Supported profile: http://interopsante.org/fhir/structuredefinition/resource/fr-practitioner<br/>Supported profile: http://medcom.dk/fhir/xds-poc/StructureDefinition/AuthorPractitioner<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.Practitioner<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-practitioner"""
    resp = requests.get(f'{FHIR_BASE}/Practitioner', params=params)
    return resp.json()

@mcp.tool
def create_practitionerrole(data: dict) -> Dict[str, Any]:
    """Create a PractitionerRole. The PractitionerRole FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/PractitionerRole<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitionerrole<br/>Supported profile: https://fhir.hl7.at/elga-austrianpatientsummary-r4/StructureDefinition/at-aps-practitionerrole<br/>Supported profile: https://nrces.in/ndhm/fhir/r4/StructureDefinition/PractitionerRole<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.PractitionerRole<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-practitioner-role"""
    resp = requests.post(f'{FHIR_BASE}/PractitionerRole', json=data)
    return resp.json()

@mcp.tool
def get_practitionerrole(resource_id: str) -> Dict[str, Any]:
    """Get a PractitionerRole by ID. The PractitionerRole FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/PractitionerRole<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitionerrole<br/>Supported profile: https://fhir.hl7.at/elga-austrianpatientsummary-r4/StructureDefinition/at-aps-practitionerrole<br/>Supported profile: https://nrces.in/ndhm/fhir/r4/StructureDefinition/PractitionerRole<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.PractitionerRole<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-practitioner-role"""
    resp = requests.get(f'{FHIR_BASE}/PractitionerRole/{resource_id}')
    return resp.json()

@mcp.tool
def search_practitionerrole(params: dict) -> Dict[str, Any]:
    """Search PractitionerRole resources. The PractitionerRole FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/PractitionerRole<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitionerrole<br/>Supported profile: https://fhir.hl7.at/elga-austrianpatientsummary-r4/StructureDefinition/at-aps-practitionerrole<br/>Supported profile: https://nrces.in/ndhm/fhir/r4/StructureDefinition/PractitionerRole<br/>Supported profile: https://profiles.ihe.net/ITI/mCSD/StructureDefinition/IHE.mCSD.PractitionerRole<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-practitioner-role"""
    resp = requests.get(f'{FHIR_BASE}/PractitionerRole', params=params)
    return resp.json()

@mcp.tool
def create_procedure(data: dict) -> Dict[str, Any]:
    """Create a Procedure. The Procedure FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Procedure<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-procedure"""
    resp = requests.post(f'{FHIR_BASE}/Procedure', json=data)
    return resp.json()

@mcp.tool
def get_procedure(resource_id: str) -> Dict[str, Any]:
    """Get a Procedure by ID. The Procedure FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Procedure<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-procedure"""
    resp = requests.get(f'{FHIR_BASE}/Procedure/{resource_id}')
    return resp.json()

@mcp.tool
def search_procedure(params: dict) -> Dict[str, Any]:
    """Search Procedure resources. The Procedure FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Procedure<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-procedure"""
    resp = requests.get(f'{FHIR_BASE}/Procedure', params=params)
    return resp.json()

@mcp.tool
def create_provenance(data: dict) -> Dict[str, Any]:
    """Create a Provenance. The Provenance FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Provenance<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-provenance<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-provenance"""
    resp = requests.post(f'{FHIR_BASE}/Provenance', json=data)
    return resp.json()

@mcp.tool
def get_provenance(resource_id: str) -> Dict[str, Any]:
    """Get a Provenance by ID. The Provenance FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Provenance<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-provenance<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-provenance"""
    resp = requests.get(f'{FHIR_BASE}/Provenance/{resource_id}')
    return resp.json()

@mcp.tool
def search_provenance(params: dict) -> Dict[str, Any]:
    """Search Provenance resources. The Provenance FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Provenance<br/>Supported profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-provenance<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-provenance"""
    resp = requests.get(f'{FHIR_BASE}/Provenance', params=params)
    return resp.json()

@mcp.tool
def create_questionnaire(data: dict) -> Dict[str, Any]:
    """Create a Questionnaire. The Questionnaire FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Questionnaire<br/>Supported profile: http://hitstdio.ntunhs.edu.tw/fhir/StructureDefinition/PCOC-Questionnaire<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-questionnaire"""
    resp = requests.post(f'{FHIR_BASE}/Questionnaire', json=data)
    return resp.json()

@mcp.tool
def get_questionnaire(resource_id: str) -> Dict[str, Any]:
    """Get a Questionnaire by ID. The Questionnaire FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Questionnaire<br/>Supported profile: http://hitstdio.ntunhs.edu.tw/fhir/StructureDefinition/PCOC-Questionnaire<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-questionnaire"""
    resp = requests.get(f'{FHIR_BASE}/Questionnaire/{resource_id}')
    return resp.json()

@mcp.tool
def search_questionnaire(params: dict) -> Dict[str, Any]:
    """Search Questionnaire resources. The Questionnaire FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Questionnaire<br/>Supported profile: http://hitstdio.ntunhs.edu.tw/fhir/StructureDefinition/PCOC-Questionnaire<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-questionnaire"""
    resp = requests.get(f'{FHIR_BASE}/Questionnaire', params=params)
    return resp.json()

@mcp.tool
def create_questionnaireresponse(data: dict) -> Dict[str, Any]:
    """Create a QuestionnaireResponse. The QuestionnaireResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-questionnaireresponse<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/svc-questionnaireresponse"""
    resp = requests.post(f'{FHIR_BASE}/QuestionnaireResponse', json=data)
    return resp.json()

@mcp.tool
def get_questionnaireresponse(resource_id: str) -> Dict[str, Any]:
    """Get a QuestionnaireResponse by ID. The QuestionnaireResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-questionnaireresponse<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/svc-questionnaireresponse"""
    resp = requests.get(f'{FHIR_BASE}/QuestionnaireResponse/{resource_id}')
    return resp.json()

@mcp.tool
def search_questionnaireresponse(params: dict) -> Dict[str, Any]:
    """Search QuestionnaireResponse resources. The QuestionnaireResponse FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/QuestionnaireResponse<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/shc-questionnaireresponse<br/>Supported profile: https://who-int.github.io/svc/refs/heads/rc2/StructureDefinition/svc-questionnaireresponse"""
    resp = requests.get(f'{FHIR_BASE}/QuestionnaireResponse', params=params)
    return resp.json()

@mcp.tool
def create_relatedperson(data: dict) -> Dict[str, Any]:
    """Create a RelatedPerson. The RelatedPerson FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/RelatedPerson<br/>Supported profile: http://ehelse.no/fhir/StructureDefinition/gd-RelatedPerson"""
    resp = requests.post(f'{FHIR_BASE}/RelatedPerson', json=data)
    return resp.json()

@mcp.tool
def get_relatedperson(resource_id: str) -> Dict[str, Any]:
    """Get a RelatedPerson by ID. The RelatedPerson FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/RelatedPerson<br/>Supported profile: http://ehelse.no/fhir/StructureDefinition/gd-RelatedPerson"""
    resp = requests.get(f'{FHIR_BASE}/RelatedPerson/{resource_id}')
    return resp.json()

@mcp.tool
def search_relatedperson(params: dict) -> Dict[str, Any]:
    """Search RelatedPerson resources. The RelatedPerson FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/RelatedPerson<br/>Supported profile: http://ehelse.no/fhir/StructureDefinition/gd-RelatedPerson"""
    resp = requests.get(f'{FHIR_BASE}/RelatedPerson', params=params)
    return resp.json()

@mcp.tool
def create_requestgroup(data: dict) -> Dict[str, Any]:
    """Create a RequestGroup. The RequestGroup FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/RequestGroup"""
    resp = requests.post(f'{FHIR_BASE}/RequestGroup', json=data)
    return resp.json()

@mcp.tool
def get_requestgroup(resource_id: str) -> Dict[str, Any]:
    """Get a RequestGroup by ID. The RequestGroup FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/RequestGroup"""
    resp = requests.get(f'{FHIR_BASE}/RequestGroup/{resource_id}')
    return resp.json()

@mcp.tool
def search_requestgroup(params: dict) -> Dict[str, Any]:
    """Search RequestGroup resources. The RequestGroup FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/RequestGroup"""
    resp = requests.get(f'{FHIR_BASE}/RequestGroup', params=params)
    return resp.json()

@mcp.tool
def create_researchdefinition(data: dict) -> Dict[str, Any]:
    """Create a ResearchDefinition. The ResearchDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ResearchDefinition"""
    resp = requests.post(f'{FHIR_BASE}/ResearchDefinition', json=data)
    return resp.json()

@mcp.tool
def get_researchdefinition(resource_id: str) -> Dict[str, Any]:
    """Get a ResearchDefinition by ID. The ResearchDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ResearchDefinition"""
    resp = requests.get(f'{FHIR_BASE}/ResearchDefinition/{resource_id}')
    return resp.json()

@mcp.tool
def search_researchdefinition(params: dict) -> Dict[str, Any]:
    """Search ResearchDefinition resources. The ResearchDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ResearchDefinition"""
    resp = requests.get(f'{FHIR_BASE}/ResearchDefinition', params=params)
    return resp.json()

@mcp.tool
def create_researchelementdefinition(data: dict) -> Dict[str, Any]:
    """Create a ResearchElementDefinition. The ResearchElementDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ResearchElementDefinition"""
    resp = requests.post(f'{FHIR_BASE}/ResearchElementDefinition', json=data)
    return resp.json()

@mcp.tool
def get_researchelementdefinition(resource_id: str) -> Dict[str, Any]:
    """Get a ResearchElementDefinition by ID. The ResearchElementDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ResearchElementDefinition"""
    resp = requests.get(f'{FHIR_BASE}/ResearchElementDefinition/{resource_id}')
    return resp.json()

@mcp.tool
def search_researchelementdefinition(params: dict) -> Dict[str, Any]:
    """Search ResearchElementDefinition resources. The ResearchElementDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ResearchElementDefinition"""
    resp = requests.get(f'{FHIR_BASE}/ResearchElementDefinition', params=params)
    return resp.json()

@mcp.tool
def create_researchstudy(data: dict) -> Dict[str, Any]:
    """Create a ResearchStudy. The ResearchStudy FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ResearchStudy"""
    resp = requests.post(f'{FHIR_BASE}/ResearchStudy', json=data)
    return resp.json()

@mcp.tool
def get_researchstudy(resource_id: str) -> Dict[str, Any]:
    """Get a ResearchStudy by ID. The ResearchStudy FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ResearchStudy"""
    resp = requests.get(f'{FHIR_BASE}/ResearchStudy/{resource_id}')
    return resp.json()

@mcp.tool
def search_researchstudy(params: dict) -> Dict[str, Any]:
    """Search ResearchStudy resources. The ResearchStudy FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ResearchStudy"""
    resp = requests.get(f'{FHIR_BASE}/ResearchStudy', params=params)
    return resp.json()

@mcp.tool
def create_researchsubject(data: dict) -> Dict[str, Any]:
    """Create a ResearchSubject. The ResearchSubject FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ResearchSubject<br/>Supported profile: http://example.org/br-and-r/soa/StructureDefinition/SOA-Subject"""
    resp = requests.post(f'{FHIR_BASE}/ResearchSubject', json=data)
    return resp.json()

@mcp.tool
def get_researchsubject(resource_id: str) -> Dict[str, Any]:
    """Get a ResearchSubject by ID. The ResearchSubject FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ResearchSubject<br/>Supported profile: http://example.org/br-and-r/soa/StructureDefinition/SOA-Subject"""
    resp = requests.get(f'{FHIR_BASE}/ResearchSubject/{resource_id}')
    return resp.json()

@mcp.tool
def search_researchsubject(params: dict) -> Dict[str, Any]:
    """Search ResearchSubject resources. The ResearchSubject FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ResearchSubject<br/>Supported profile: http://example.org/br-and-r/soa/StructureDefinition/SOA-Subject"""
    resp = requests.get(f'{FHIR_BASE}/ResearchSubject', params=params)
    return resp.json()

@mcp.tool
def create_riskassessment(data: dict) -> Dict[str, Any]:
    """Create a RiskAssessment. The RiskAssessment FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/RiskAssessment"""
    resp = requests.post(f'{FHIR_BASE}/RiskAssessment', json=data)
    return resp.json()

@mcp.tool
def get_riskassessment(resource_id: str) -> Dict[str, Any]:
    """Get a RiskAssessment by ID. The RiskAssessment FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/RiskAssessment"""
    resp = requests.get(f'{FHIR_BASE}/RiskAssessment/{resource_id}')
    return resp.json()

@mcp.tool
def search_riskassessment(params: dict) -> Dict[str, Any]:
    """Search RiskAssessment resources. The RiskAssessment FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/RiskAssessment"""
    resp = requests.get(f'{FHIR_BASE}/RiskAssessment', params=params)
    return resp.json()

@mcp.tool
def create_riskevidencesynthesis(data: dict) -> Dict[str, Any]:
    """Create a RiskEvidenceSynthesis. The RiskEvidenceSynthesis FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/RiskEvidenceSynthesis"""
    resp = requests.post(f'{FHIR_BASE}/RiskEvidenceSynthesis', json=data)
    return resp.json()

@mcp.tool
def get_riskevidencesynthesis(resource_id: str) -> Dict[str, Any]:
    """Get a RiskEvidenceSynthesis by ID. The RiskEvidenceSynthesis FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/RiskEvidenceSynthesis"""
    resp = requests.get(f'{FHIR_BASE}/RiskEvidenceSynthesis/{resource_id}')
    return resp.json()

@mcp.tool
def search_riskevidencesynthesis(params: dict) -> Dict[str, Any]:
    """Search RiskEvidenceSynthesis resources. The RiskEvidenceSynthesis FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/RiskEvidenceSynthesis"""
    resp = requests.get(f'{FHIR_BASE}/RiskEvidenceSynthesis', params=params)
    return resp.json()

@mcp.tool
def create_schedule(data: dict) -> Dict[str, Any]:
    """Create a Schedule. The Schedule FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Schedule"""
    resp = requests.post(f'{FHIR_BASE}/Schedule', json=data)
    return resp.json()

@mcp.tool
def get_schedule(resource_id: str) -> Dict[str, Any]:
    """Get a Schedule by ID. The Schedule FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Schedule"""
    resp = requests.get(f'{FHIR_BASE}/Schedule/{resource_id}')
    return resp.json()

@mcp.tool
def search_schedule(params: dict) -> Dict[str, Any]:
    """Search Schedule resources. The Schedule FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Schedule"""
    resp = requests.get(f'{FHIR_BASE}/Schedule', params=params)
    return resp.json()

@mcp.tool
def create_searchparameter(data: dict) -> Dict[str, Any]:
    """Create a SearchParameter. The SearchParameter FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SearchParameter<br/>Supported profile: http://fhir.gevko.de/fhir/StructureDefinition/storniert"""
    resp = requests.post(f'{FHIR_BASE}/SearchParameter', json=data)
    return resp.json()

@mcp.tool
def get_searchparameter(resource_id: str) -> Dict[str, Any]:
    """Get a SearchParameter by ID. The SearchParameter FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SearchParameter<br/>Supported profile: http://fhir.gevko.de/fhir/StructureDefinition/storniert"""
    resp = requests.get(f'{FHIR_BASE}/SearchParameter/{resource_id}')
    return resp.json()

@mcp.tool
def search_searchparameter(params: dict) -> Dict[str, Any]:
    """Search SearchParameter resources. The SearchParameter FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SearchParameter<br/>Supported profile: http://fhir.gevko.de/fhir/StructureDefinition/storniert"""
    resp = requests.get(f'{FHIR_BASE}/SearchParameter', params=params)
    return resp.json()

@mcp.tool
def create_servicerequest(data: dict) -> Dict[str, Any]:
    """Create a ServiceRequest. The ServiceRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ServiceRequest<br/>Supported profile: http://example.org/fhir/StructureDefinition/ColonoscopyReferralProfile<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/servicerequest"""
    resp = requests.post(f'{FHIR_BASE}/ServiceRequest', json=data)
    return resp.json()

@mcp.tool
def get_servicerequest(resource_id: str) -> Dict[str, Any]:
    """Get a ServiceRequest by ID. The ServiceRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ServiceRequest<br/>Supported profile: http://example.org/fhir/StructureDefinition/ColonoscopyReferralProfile<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/servicerequest"""
    resp = requests.get(f'{FHIR_BASE}/ServiceRequest/{resource_id}')
    return resp.json()

@mcp.tool
def search_servicerequest(params: dict) -> Dict[str, Any]:
    """Search ServiceRequest resources. The ServiceRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ServiceRequest<br/>Supported profile: http://example.org/fhir/StructureDefinition/ColonoscopyReferralProfile<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/servicerequest"""
    resp = requests.get(f'{FHIR_BASE}/ServiceRequest', params=params)
    return resp.json()

@mcp.tool
def create_slot(data: dict) -> Dict[str, Any]:
    """Create a Slot. The Slot FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Slot"""
    resp = requests.post(f'{FHIR_BASE}/Slot', json=data)
    return resp.json()

@mcp.tool
def get_slot(resource_id: str) -> Dict[str, Any]:
    """Get a Slot by ID. The Slot FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Slot"""
    resp = requests.get(f'{FHIR_BASE}/Slot/{resource_id}')
    return resp.json()

@mcp.tool
def search_slot(params: dict) -> Dict[str, Any]:
    """Search Slot resources. The Slot FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Slot"""
    resp = requests.get(f'{FHIR_BASE}/Slot', params=params)
    return resp.json()

@mcp.tool
def create_specimen(data: dict) -> Dict[str, Any]:
    """Create a Specimen. The Specimen FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Specimen<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/specimen"""
    resp = requests.post(f'{FHIR_BASE}/Specimen', json=data)
    return resp.json()

@mcp.tool
def get_specimen(resource_id: str) -> Dict[str, Any]:
    """Get a Specimen by ID. The Specimen FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Specimen<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/specimen"""
    resp = requests.get(f'{FHIR_BASE}/Specimen/{resource_id}')
    return resp.json()

@mcp.tool
def search_specimen(params: dict) -> Dict[str, Any]:
    """Search Specimen resources. The Specimen FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Specimen<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/specimen"""
    resp = requests.get(f'{FHIR_BASE}/Specimen', params=params)
    return resp.json()

@mcp.tool
def create_specimendefinition(data: dict) -> Dict[str, Any]:
    """Create a SpecimenDefinition. The SpecimenDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SpecimenDefinition"""
    resp = requests.post(f'{FHIR_BASE}/SpecimenDefinition', json=data)
    return resp.json()

@mcp.tool
def get_specimendefinition(resource_id: str) -> Dict[str, Any]:
    """Get a SpecimenDefinition by ID. The SpecimenDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SpecimenDefinition"""
    resp = requests.get(f'{FHIR_BASE}/SpecimenDefinition/{resource_id}')
    return resp.json()

@mcp.tool
def search_specimendefinition(params: dict) -> Dict[str, Any]:
    """Search SpecimenDefinition resources. The SpecimenDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SpecimenDefinition"""
    resp = requests.get(f'{FHIR_BASE}/SpecimenDefinition', params=params)
    return resp.json()

@mcp.tool
def create_structuredefinition(data: dict) -> Dict[str, Any]:
    """Create a StructureDefinition. The StructureDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/StructureDefinition<br/>Supported profile: http://sap.com/healthcare/PatActg/fhir/StructureDefinition/BusinessConfigurationStructureDefinition"""
    resp = requests.post(f'{FHIR_BASE}/StructureDefinition', json=data)
    return resp.json()

@mcp.tool
def get_structuredefinition(resource_id: str) -> Dict[str, Any]:
    """Get a StructureDefinition by ID. The StructureDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/StructureDefinition<br/>Supported profile: http://sap.com/healthcare/PatActg/fhir/StructureDefinition/BusinessConfigurationStructureDefinition"""
    resp = requests.get(f'{FHIR_BASE}/StructureDefinition/{resource_id}')
    return resp.json()

@mcp.tool
def search_structuredefinition(params: dict) -> Dict[str, Any]:
    """Search StructureDefinition resources. The StructureDefinition FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/StructureDefinition<br/>Supported profile: http://sap.com/healthcare/PatActg/fhir/StructureDefinition/BusinessConfigurationStructureDefinition"""
    resp = requests.get(f'{FHIR_BASE}/StructureDefinition', params=params)
    return resp.json()

@mcp.tool
def create_structuremap(data: dict) -> Dict[str, Any]:
    """Create a StructureMap. The StructureMap FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/StructureMap"""
    resp = requests.post(f'{FHIR_BASE}/StructureMap', json=data)
    return resp.json()

@mcp.tool
def get_structuremap(resource_id: str) -> Dict[str, Any]:
    """Get a StructureMap by ID. The StructureMap FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/StructureMap"""
    resp = requests.get(f'{FHIR_BASE}/StructureMap/{resource_id}')
    return resp.json()

@mcp.tool
def search_structuremap(params: dict) -> Dict[str, Any]:
    """Search StructureMap resources. The StructureMap FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/StructureMap"""
    resp = requests.get(f'{FHIR_BASE}/StructureMap', params=params)
    return resp.json()

@mcp.tool
def create_subscription(data: dict) -> Dict[str, Any]:
    """Create a Subscription. The Subscription FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Subscription<br/>Supported profile: http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-subscription"""
    resp = requests.post(f'{FHIR_BASE}/Subscription', json=data)
    return resp.json()

@mcp.tool
def get_subscription(resource_id: str) -> Dict[str, Any]:
    """Get a Subscription by ID. The Subscription FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Subscription<br/>Supported profile: http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-subscription"""
    resp = requests.get(f'{FHIR_BASE}/Subscription/{resource_id}')
    return resp.json()

@mcp.tool
def search_subscription(params: dict) -> Dict[str, Any]:
    """Search Subscription resources. The Subscription FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Subscription<br/>Supported profile: http://hl7.org/fhir/uv/subscriptions-backport/StructureDefinition/backport-subscription"""
    resp = requests.get(f'{FHIR_BASE}/Subscription', params=params)
    return resp.json()

@mcp.tool
def create_substance(data: dict) -> Dict[str, Any]:
    """Create a Substance. The Substance FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Substance"""
    resp = requests.post(f'{FHIR_BASE}/Substance', json=data)
    return resp.json()

@mcp.tool
def get_substance(resource_id: str) -> Dict[str, Any]:
    """Get a Substance by ID. The Substance FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Substance"""
    resp = requests.get(f'{FHIR_BASE}/Substance/{resource_id}')
    return resp.json()

@mcp.tool
def search_substance(params: dict) -> Dict[str, Any]:
    """Search Substance resources. The Substance FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Substance"""
    resp = requests.get(f'{FHIR_BASE}/Substance', params=params)
    return resp.json()

@mcp.tool
def create_substancenucleicacid(data: dict) -> Dict[str, Any]:
    """Create a SubstanceNucleicAcid. The SubstanceNucleicAcid FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstanceNucleicAcid"""
    resp = requests.post(f'{FHIR_BASE}/SubstanceNucleicAcid', json=data)
    return resp.json()

@mcp.tool
def get_substancenucleicacid(resource_id: str) -> Dict[str, Any]:
    """Get a SubstanceNucleicAcid by ID. The SubstanceNucleicAcid FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstanceNucleicAcid"""
    resp = requests.get(f'{FHIR_BASE}/SubstanceNucleicAcid/{resource_id}')
    return resp.json()

@mcp.tool
def search_substancenucleicacid(params: dict) -> Dict[str, Any]:
    """Search SubstanceNucleicAcid resources. The SubstanceNucleicAcid FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstanceNucleicAcid"""
    resp = requests.get(f'{FHIR_BASE}/SubstanceNucleicAcid', params=params)
    return resp.json()

@mcp.tool
def create_substancepolymer(data: dict) -> Dict[str, Any]:
    """Create a SubstancePolymer. The SubstancePolymer FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstancePolymer"""
    resp = requests.post(f'{FHIR_BASE}/SubstancePolymer', json=data)
    return resp.json()

@mcp.tool
def get_substancepolymer(resource_id: str) -> Dict[str, Any]:
    """Get a SubstancePolymer by ID. The SubstancePolymer FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstancePolymer"""
    resp = requests.get(f'{FHIR_BASE}/SubstancePolymer/{resource_id}')
    return resp.json()

@mcp.tool
def search_substancepolymer(params: dict) -> Dict[str, Any]:
    """Search SubstancePolymer resources. The SubstancePolymer FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstancePolymer"""
    resp = requests.get(f'{FHIR_BASE}/SubstancePolymer', params=params)
    return resp.json()

@mcp.tool
def create_substanceprotein(data: dict) -> Dict[str, Any]:
    """Create a SubstanceProtein. The SubstanceProtein FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstanceProtein"""
    resp = requests.post(f'{FHIR_BASE}/SubstanceProtein', json=data)
    return resp.json()

@mcp.tool
def get_substanceprotein(resource_id: str) -> Dict[str, Any]:
    """Get a SubstanceProtein by ID. The SubstanceProtein FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstanceProtein"""
    resp = requests.get(f'{FHIR_BASE}/SubstanceProtein/{resource_id}')
    return resp.json()

@mcp.tool
def search_substanceprotein(params: dict) -> Dict[str, Any]:
    """Search SubstanceProtein resources. The SubstanceProtein FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstanceProtein"""
    resp = requests.get(f'{FHIR_BASE}/SubstanceProtein', params=params)
    return resp.json()

@mcp.tool
def create_substancereferenceinformation(data: dict) -> Dict[str, Any]:
    """Create a SubstanceReferenceInformation. The SubstanceReferenceInformation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstanceReferenceInformation"""
    resp = requests.post(f'{FHIR_BASE}/SubstanceReferenceInformation', json=data)
    return resp.json()

@mcp.tool
def get_substancereferenceinformation(resource_id: str) -> Dict[str, Any]:
    """Get a SubstanceReferenceInformation by ID. The SubstanceReferenceInformation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstanceReferenceInformation"""
    resp = requests.get(f'{FHIR_BASE}/SubstanceReferenceInformation/{resource_id}')
    return resp.json()

@mcp.tool
def search_substancereferenceinformation(params: dict) -> Dict[str, Any]:
    """Search SubstanceReferenceInformation resources. The SubstanceReferenceInformation FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstanceReferenceInformation"""
    resp = requests.get(f'{FHIR_BASE}/SubstanceReferenceInformation', params=params)
    return resp.json()

@mcp.tool
def create_substancesourcematerial(data: dict) -> Dict[str, Any]:
    """Create a SubstanceSourceMaterial. The SubstanceSourceMaterial FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstanceSourceMaterial"""
    resp = requests.post(f'{FHIR_BASE}/SubstanceSourceMaterial', json=data)
    return resp.json()

@mcp.tool
def get_substancesourcematerial(resource_id: str) -> Dict[str, Any]:
    """Get a SubstanceSourceMaterial by ID. The SubstanceSourceMaterial FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstanceSourceMaterial"""
    resp = requests.get(f'{FHIR_BASE}/SubstanceSourceMaterial/{resource_id}')
    return resp.json()

@mcp.tool
def search_substancesourcematerial(params: dict) -> Dict[str, Any]:
    """Search SubstanceSourceMaterial resources. The SubstanceSourceMaterial FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstanceSourceMaterial"""
    resp = requests.get(f'{FHIR_BASE}/SubstanceSourceMaterial', params=params)
    return resp.json()

@mcp.tool
def create_substancespecification(data: dict) -> Dict[str, Any]:
    """Create a SubstanceSpecification. The SubstanceSpecification FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstanceSpecification"""
    resp = requests.post(f'{FHIR_BASE}/SubstanceSpecification', json=data)
    return resp.json()

@mcp.tool
def get_substancespecification(resource_id: str) -> Dict[str, Any]:
    """Get a SubstanceSpecification by ID. The SubstanceSpecification FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstanceSpecification"""
    resp = requests.get(f'{FHIR_BASE}/SubstanceSpecification/{resource_id}')
    return resp.json()

@mcp.tool
def search_substancespecification(params: dict) -> Dict[str, Any]:
    """Search SubstanceSpecification resources. The SubstanceSpecification FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SubstanceSpecification"""
    resp = requests.get(f'{FHIR_BASE}/SubstanceSpecification', params=params)
    return resp.json()

@mcp.tool
def create_supplydelivery(data: dict) -> Dict[str, Any]:
    """Create a SupplyDelivery. The SupplyDelivery FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SupplyDelivery"""
    resp = requests.post(f'{FHIR_BASE}/SupplyDelivery', json=data)
    return resp.json()

@mcp.tool
def get_supplydelivery(resource_id: str) -> Dict[str, Any]:
    """Get a SupplyDelivery by ID. The SupplyDelivery FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SupplyDelivery"""
    resp = requests.get(f'{FHIR_BASE}/SupplyDelivery/{resource_id}')
    return resp.json()

@mcp.tool
def search_supplydelivery(params: dict) -> Dict[str, Any]:
    """Search SupplyDelivery resources. The SupplyDelivery FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SupplyDelivery"""
    resp = requests.get(f'{FHIR_BASE}/SupplyDelivery', params=params)
    return resp.json()

@mcp.tool
def create_supplyrequest(data: dict) -> Dict[str, Any]:
    """Create a SupplyRequest. The SupplyRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SupplyRequest"""
    resp = requests.post(f'{FHIR_BASE}/SupplyRequest', json=data)
    return resp.json()

@mcp.tool
def get_supplyrequest(resource_id: str) -> Dict[str, Any]:
    """Get a SupplyRequest by ID. The SupplyRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SupplyRequest"""
    resp = requests.get(f'{FHIR_BASE}/SupplyRequest/{resource_id}')
    return resp.json()

@mcp.tool
def search_supplyrequest(params: dict) -> Dict[str, Any]:
    """Search SupplyRequest resources. The SupplyRequest FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/SupplyRequest"""
    resp = requests.get(f'{FHIR_BASE}/SupplyRequest', params=params)
    return resp.json()

@mcp.tool
def create_task(data: dict) -> Dict[str, Any]:
    """Create a Task. The Task FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Task<br/>Supported profile: http://example.org/fhir/StructureDefinition/MyKTTask<br/>Supported profile: http://hl7.org/fhir/us/davinci-cdex/StructureDefinition/cdex-task<br/>Supported profile: http://hl7.org/fhir/us/davinci-pcde/StructureDefinition/profile-task-request<br/>Supported profile: http://hl7.org/fhir/us/dme-orders/StructureDefinition/PAO-task4<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/task-med-chg<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/task-rec-followup"""
    resp = requests.post(f'{FHIR_BASE}/Task', json=data)
    return resp.json()

@mcp.tool
def get_task(resource_id: str) -> Dict[str, Any]:
    """Get a Task by ID. The Task FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Task<br/>Supported profile: http://example.org/fhir/StructureDefinition/MyKTTask<br/>Supported profile: http://hl7.org/fhir/us/davinci-cdex/StructureDefinition/cdex-task<br/>Supported profile: http://hl7.org/fhir/us/davinci-pcde/StructureDefinition/profile-task-request<br/>Supported profile: http://hl7.org/fhir/us/dme-orders/StructureDefinition/PAO-task4<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/task-med-chg<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/task-rec-followup"""
    resp = requests.get(f'{FHIR_BASE}/Task/{resource_id}')
    return resp.json()

@mcp.tool
def search_task(params: dict) -> Dict[str, Any]:
    """Search Task resources. The Task FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/Task<br/>Supported profile: http://example.org/fhir/StructureDefinition/MyKTTask<br/>Supported profile: http://hl7.org/fhir/us/davinci-cdex/StructureDefinition/cdex-task<br/>Supported profile: http://hl7.org/fhir/us/davinci-pcde/StructureDefinition/profile-task-request<br/>Supported profile: http://hl7.org/fhir/us/dme-orders/StructureDefinition/PAO-task4<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/task-med-chg<br/>Supported profile: http://hl7.org/fhir/uv/genomics-reporting/StructureDefinition/task-rec-followup"""
    resp = requests.get(f'{FHIR_BASE}/Task', params=params)
    return resp.json()

@mcp.tool
def create_terminologycapabilities(data: dict) -> Dict[str, Any]:
    """Create a TerminologyCapabilities. The TerminologyCapabilities FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/TerminologyCapabilities"""
    resp = requests.post(f'{FHIR_BASE}/TerminologyCapabilities', json=data)
    return resp.json()

@mcp.tool
def get_terminologycapabilities(resource_id: str) -> Dict[str, Any]:
    """Get a TerminologyCapabilities by ID. The TerminologyCapabilities FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/TerminologyCapabilities"""
    resp = requests.get(f'{FHIR_BASE}/TerminologyCapabilities/{resource_id}')
    return resp.json()

@mcp.tool
def search_terminologycapabilities(params: dict) -> Dict[str, Any]:
    """Search TerminologyCapabilities resources. The TerminologyCapabilities FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/TerminologyCapabilities"""
    resp = requests.get(f'{FHIR_BASE}/TerminologyCapabilities', params=params)
    return resp.json()

@mcp.tool
def create_testreport(data: dict) -> Dict[str, Any]:
    """Create a TestReport. The TestReport FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/TestReport"""
    resp = requests.post(f'{FHIR_BASE}/TestReport', json=data)
    return resp.json()

@mcp.tool
def get_testreport(resource_id: str) -> Dict[str, Any]:
    """Get a TestReport by ID. The TestReport FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/TestReport"""
    resp = requests.get(f'{FHIR_BASE}/TestReport/{resource_id}')
    return resp.json()

@mcp.tool
def search_testreport(params: dict) -> Dict[str, Any]:
    """Search TestReport resources. The TestReport FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/TestReport"""
    resp = requests.get(f'{FHIR_BASE}/TestReport', params=params)
    return resp.json()

@mcp.tool
def create_testscript(data: dict) -> Dict[str, Any]:
    """Create a TestScript. The TestScript FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/TestScript"""
    resp = requests.post(f'{FHIR_BASE}/TestScript', json=data)
    return resp.json()

@mcp.tool
def get_testscript(resource_id: str) -> Dict[str, Any]:
    """Get a TestScript by ID. The TestScript FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/TestScript"""
    resp = requests.get(f'{FHIR_BASE}/TestScript/{resource_id}')
    return resp.json()

@mcp.tool
def search_testscript(params: dict) -> Dict[str, Any]:
    """Search TestScript resources. The TestScript FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/TestScript"""
    resp = requests.get(f'{FHIR_BASE}/TestScript', params=params)
    return resp.json()

@mcp.tool
def create_valueset(data: dict) -> Dict[str, Any]:
    """Create a ValueSet. The ValueSet FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ValueSet"""
    resp = requests.post(f'{FHIR_BASE}/ValueSet', json=data)
    return resp.json()

@mcp.tool
def get_valueset(resource_id: str) -> Dict[str, Any]:
    """Get a ValueSet by ID. The ValueSet FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ValueSet"""
    resp = requests.get(f'{FHIR_BASE}/ValueSet/{resource_id}')
    return resp.json()

@mcp.tool
def search_valueset(params: dict) -> Dict[str, Any]:
    """Search ValueSet resources. The ValueSet FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/ValueSet"""
    resp = requests.get(f'{FHIR_BASE}/ValueSet', params=params)
    return resp.json()

@mcp.tool
def create_verificationresult(data: dict) -> Dict[str, Any]:
    """Create a VerificationResult. The VerificationResult FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/VerificationResult"""
    resp = requests.post(f'{FHIR_BASE}/VerificationResult', json=data)
    return resp.json()

@mcp.tool
def get_verificationresult(resource_id: str) -> Dict[str, Any]:
    """Get a VerificationResult by ID. The VerificationResult FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/VerificationResult"""
    resp = requests.get(f'{FHIR_BASE}/VerificationResult/{resource_id}')
    return resp.json()

@mcp.tool
def search_verificationresult(params: dict) -> Dict[str, Any]:
    """Search VerificationResult resources. The VerificationResult FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/VerificationResult"""
    resp = requests.get(f'{FHIR_BASE}/VerificationResult', params=params)
    return resp.json()

@mcp.tool
def create_visionprescription(data: dict) -> Dict[str, Any]:
    """Create a VisionPrescription. The VisionPrescription FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/VisionPrescription"""
    resp = requests.post(f'{FHIR_BASE}/VisionPrescription', json=data)
    return resp.json()

@mcp.tool
def get_visionprescription(resource_id: str) -> Dict[str, Any]:
    """Get a VisionPrescription by ID. The VisionPrescription FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/VisionPrescription"""
    resp = requests.get(f'{FHIR_BASE}/VisionPrescription/{resource_id}')
    return resp.json()

@mcp.tool
def search_visionprescription(params: dict) -> Dict[str, Any]:
    """Search VisionPrescription resources. The VisionPrescription FHIR resource type<br/>Base profile: http://hl7.org/fhir/StructureDefinition/VisionPrescription"""
    resp = requests.get(f'{FHIR_BASE}/VisionPrescription', params=params)
    return resp.json()

if __name__ == '__main__':
    mcp.run(host='0.0.0.0', port=8085)
