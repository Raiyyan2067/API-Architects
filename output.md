[01;34m.[0m
├── Dockerfile
├── README.md
├── [01;34mapp[0m
│   ├── __init__.py
│   ├── [01;34m__pycache__[0m
│   │   ├── __init__.cpython-312.pyc
│   │   └── main.cpython-312.pyc
│   ├── [01;34mapi[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   └── __init__.cpython-312.pyc
│   │   └── [01;34mv1[0m
│   │       ├── [01;34m__pycache__[0m
│   │       │   ├── despatch.cpython-312.pyc
│   │       │   └── health.cpython-312.pyc
│   │       ├── despatch.py
│   │       └── health.py
│   ├── [01;34mcore[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── ubl_generator.cpython-312.pyc
│   │   ├── config.py
│   │   ├── ubl_generator.py
│   │   └── xml_validator.py
│   ├── [01;34mdata[0m
│   │   └── mock_orders.json
│   ├── main.py
│   ├── [01;34mmodels[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── despatch_models.cpython-312.pyc
│   │   └── despatch_models.py
│   ├── [01;34mtemplates[0m
│   │   └── despatch_advice_template.xml
│   └── [01;34mxsd[0m
│       ├── [01;34mcommon[0m
│       │   ├── CCTS_CCT_SchemaModule-2.1.xsd
│       │   ├── UBL-CommonAggregateComponents-2.1.xsd
│       │   ├── UBL-CommonBasicComponents-2.1.xsd
│       │   ├── UBL-CommonExtensionComponents-2.1.xsd
│       │   ├── UBL-CommonSignatureComponents-2.1.xsd
│       │   ├── UBL-CoreComponentParameters-2.1.xsd
│       │   ├── UBL-ExtensionContentDataType-2.1.xsd
│       │   ├── UBL-QualifiedDataTypes-2.1.xsd
│       │   ├── UBL-SignatureAggregateComponents-2.1.xsd
│       │   ├── UBL-SignatureBasicComponents-2.1.xsd
│       │   ├── UBL-UnqualifiedDataTypes-2.1.xsd
│       │   ├── UBL-XAdESv132-2.1.xsd
│       │   ├── UBL-XAdESv141-2.1.xsd
│       │   └── UBL-xmldsig-core-schema-2.1.xsd
│       └── [01;34mmaindoc[0m
│           ├── UBL-ApplicationResponse-2.1.xsd
│           ├── UBL-AttachedDocument-2.1.xsd
│           ├── UBL-AwardedNotification-2.1.xsd
│           ├── UBL-BillOfLading-2.1.xsd
│           ├── UBL-CallForTenders-2.1.xsd
│           ├── UBL-Catalogue-2.1.xsd
│           ├── UBL-CatalogueDeletion-2.1.xsd
│           ├── UBL-CatalogueItemSpecificationUpdate-2.1.xsd
│           ├── UBL-CataloguePricingUpdate-2.1.xsd
│           ├── UBL-CatalogueRequest-2.1.xsd
│           ├── UBL-CertificateOfOrigin-2.1.xsd
│           ├── UBL-ContractAwardNotice-2.1.xsd
│           ├── UBL-ContractNotice-2.1.xsd
│           ├── UBL-CreditNote-2.1.xsd
│           ├── UBL-DebitNote-2.1.xsd
│           ├── UBL-DespatchAdvice-2.1.xsd
│           ├── UBL-DocumentStatus-2.1.xsd
│           ├── UBL-DocumentStatusRequest-2.1.xsd
│           ├── UBL-ExceptionCriteria-2.1.xsd
│           ├── UBL-ExceptionNotification-2.1.xsd
│           ├── UBL-Forecast-2.1.xsd
│           ├── UBL-ForecastRevision-2.1.xsd
│           ├── UBL-ForwardingInstructions-2.1.xsd
│           ├── UBL-FreightInvoice-2.1.xsd
│           ├── UBL-FulfilmentCancellation-2.1.xsd
│           ├── UBL-GoodsItemItinerary-2.1.xsd
│           ├── UBL-GuaranteeCertificate-2.1.xsd
│           ├── UBL-InstructionForReturns-2.1.xsd
│           ├── UBL-InventoryReport-2.1.xsd
│           ├── UBL-Invoice-2.1.xsd
│           ├── UBL-ItemInformationRequest-2.1.xsd
│           ├── UBL-Order-2.1.xsd
│           ├── UBL-OrderCancellation-2.1.xsd
│           ├── UBL-OrderChange-2.1.xsd
│           ├── UBL-OrderResponse-2.1.xsd
│           ├── UBL-OrderResponseSimple-2.1.xsd
│           ├── UBL-PackingList-2.1.xsd
│           ├── UBL-PriorInformationNotice-2.1.xsd
│           ├── UBL-ProductActivity-2.1.xsd
│           ├── UBL-Quotation-2.1.xsd
│           ├── UBL-ReceiptAdvice-2.1.xsd
│           ├── UBL-Reminder-2.1.xsd
│           ├── UBL-RemittanceAdvice-2.1.xsd
│           ├── UBL-RequestForQuotation-2.1.xsd
│           ├── UBL-RetailEvent-2.1.xsd
│           ├── UBL-SelfBilledCreditNote-2.1.xsd
│           ├── UBL-SelfBilledInvoice-2.1.xsd
│           ├── UBL-Statement-2.1.xsd
│           ├── UBL-StockAvailabilityReport-2.1.xsd
│           ├── UBL-Tender-2.1.xsd
│           ├── UBL-TenderReceipt-2.1.xsd
│           ├── UBL-TendererQualification-2.1.xsd
│           ├── UBL-TendererQualificationResponse-2.1.xsd
│           ├── UBL-TradeItemLocationProfile-2.1.xsd
│           ├── UBL-TransportExecutionPlan-2.1.xsd
│           ├── UBL-TransportExecutionPlanRequest-2.1.xsd
│           ├── UBL-TransportProgressStatus-2.1.xsd
│           ├── UBL-TransportProgressStatusRequest-2.1.xsd
│           ├── UBL-TransportServiceDescription-2.1.xsd
│           ├── UBL-TransportServiceDescriptionRequest-2.1.xsd
│           ├── UBL-TransportationStatus-2.1.xsd
│           ├── UBL-TransportationStatusRequest-2.1.xsd
│           ├── UBL-UnawardedNotification-2.1.xsd
│           ├── UBL-UtilityStatement-2.1.xsd
│           └── UBL-Waybill-2.1.xsd
├── [01;34mgenerated[0m
├── manual_test.py
├── output.md
├── output_despatch.xml
├── [01;34mpackage[0m
│   ├── [01;34m__pycache__[0m
│   │   ├── py.cpython-312.pyc
│   │   └── typing_extensions.cpython-312.pyc
│   ├── [01;34m_pytest[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── _argcomplete.cpython-312.pyc
│   │   │   ├── _version.cpython-312.pyc
│   │   │   ├── cacheprovider.cpython-312.pyc
│   │   │   ├── capture.cpython-312.pyc
│   │   │   ├── compat.cpython-312.pyc
│   │   │   ├── debugging.cpython-312.pyc
│   │   │   ├── deprecated.cpython-312.pyc
│   │   │   ├── doctest.cpython-312.pyc
│   │   │   ├── faulthandler.cpython-312.pyc
│   │   │   ├── fixtures.cpython-312.pyc
│   │   │   ├── freeze_support.cpython-312.pyc
│   │   │   ├── helpconfig.cpython-312.pyc
│   │   │   ├── hookspec.cpython-312.pyc
│   │   │   ├── junitxml.cpython-312.pyc
│   │   │   ├── legacypath.cpython-312.pyc
│   │   │   ├── logging.cpython-312.pyc
│   │   │   ├── main.cpython-312.pyc
│   │   │   ├── monkeypatch.cpython-312.pyc
│   │   │   ├── nodes.cpython-312.pyc
│   │   │   ├── outcomes.cpython-312.pyc
│   │   │   ├── pastebin.cpython-312.pyc
│   │   │   ├── pathlib.cpython-312.pyc
│   │   │   ├── pytester.cpython-312.pyc
│   │   │   ├── pytester_assertions.cpython-312.pyc
│   │   │   ├── python.cpython-312.pyc
│   │   │   ├── python_api.cpython-312.pyc
│   │   │   ├── raises.cpython-312.pyc
│   │   │   ├── recwarn.cpython-312.pyc
│   │   │   ├── reports.cpython-312.pyc
│   │   │   ├── runner.cpython-312.pyc
│   │   │   ├── scope.cpython-312.pyc
│   │   │   ├── setuponly.cpython-312.pyc
│   │   │   ├── setupplan.cpython-312.pyc
│   │   │   ├── skipping.cpython-312.pyc
│   │   │   ├── stash.cpython-312.pyc
│   │   │   ├── stepwise.cpython-312.pyc
│   │   │   ├── subtests.cpython-312.pyc
│   │   │   ├── terminal.cpython-312.pyc
│   │   │   ├── terminalprogress.cpython-312.pyc
│   │   │   ├── threadexception.cpython-312.pyc
│   │   │   ├── timing.cpython-312.pyc
│   │   │   ├── tmpdir.cpython-312.pyc
│   │   │   ├── tracemalloc.cpython-312.pyc
│   │   │   ├── unittest.cpython-312.pyc
│   │   │   ├── unraisableexception.cpython-312.pyc
│   │   │   ├── warning_types.cpython-312.pyc
│   │   │   └── warnings.cpython-312.pyc
│   │   ├── _argcomplete.py
│   │   ├── [01;34m_code[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── code.cpython-312.pyc
│   │   │   │   └── source.cpython-312.pyc
│   │   │   ├── code.py
│   │   │   └── source.py
│   │   ├── [01;34m_io[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── pprint.cpython-312.pyc
│   │   │   │   ├── saferepr.cpython-312.pyc
│   │   │   │   ├── terminalwriter.cpython-312.pyc
│   │   │   │   └── wcwidth.cpython-312.pyc
│   │   │   ├── pprint.py
│   │   │   ├── saferepr.py
│   │   │   ├── terminalwriter.py
│   │   │   └── wcwidth.py
│   │   ├── [01;34m_py[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── error.cpython-312.pyc
│   │   │   │   └── path.cpython-312.pyc
│   │   │   ├── error.py
│   │   │   └── path.py
│   │   ├── _version.py
│   │   ├── [01;34massertion[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── rewrite.cpython-312.pyc
│   │   │   │   ├── truncate.cpython-312.pyc
│   │   │   │   └── util.cpython-312.pyc
│   │   │   ├── rewrite.py
│   │   │   ├── truncate.py
│   │   │   └── util.py
│   │   ├── cacheprovider.py
│   │   ├── capture.py
│   │   ├── compat.py
│   │   ├── [01;34mconfig[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── argparsing.cpython-312.pyc
│   │   │   │   ├── compat.cpython-312.pyc
│   │   │   │   ├── exceptions.cpython-312.pyc
│   │   │   │   └── findpaths.cpython-312.pyc
│   │   │   ├── argparsing.py
│   │   │   ├── compat.py
│   │   │   ├── exceptions.py
│   │   │   └── findpaths.py
│   │   ├── debugging.py
│   │   ├── deprecated.py
│   │   ├── doctest.py
│   │   ├── faulthandler.py
│   │   ├── fixtures.py
│   │   ├── freeze_support.py
│   │   ├── helpconfig.py
│   │   ├── hookspec.py
│   │   ├── junitxml.py
│   │   ├── legacypath.py
│   │   ├── logging.py
│   │   ├── main.py
│   │   ├── [01;34mmark[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── expression.cpython-312.pyc
│   │   │   │   └── structures.cpython-312.pyc
│   │   │   ├── expression.py
│   │   │   └── structures.py
│   │   ├── monkeypatch.py
│   │   ├── nodes.py
│   │   ├── outcomes.py
│   │   ├── pastebin.py
│   │   ├── pathlib.py
│   │   ├── py.typed
│   │   ├── pytester.py
│   │   ├── pytester_assertions.py
│   │   ├── python.py
│   │   ├── python_api.py
│   │   ├── raises.py
│   │   ├── recwarn.py
│   │   ├── reports.py
│   │   ├── runner.py
│   │   ├── scope.py
│   │   ├── setuponly.py
│   │   ├── setupplan.py
│   │   ├── skipping.py
│   │   ├── stash.py
│   │   ├── stepwise.py
│   │   ├── subtests.py
│   │   ├── terminal.py
│   │   ├── terminalprogress.py
│   │   ├── threadexception.py
│   │   ├── timing.py
│   │   ├── tmpdir.py
│   │   ├── tracemalloc.py
│   │   ├── unittest.py
│   │   ├── unraisableexception.py
│   │   ├── warning_types.py
│   │   └── warnings.py
│   ├── [01;34mannotated_doc[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── main.cpython-312.pyc
│   │   ├── main.py
│   │   └── py.typed
│   ├── [01;34mannotated_doc-0.0.4.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   ├── entry_points.txt
│   │   └── [01;34mlicenses[0m
│   │       └── LICENSE
│   ├── [01;34mannotated_types[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── test_cases.cpython-312.pyc
│   │   ├── py.typed
│   │   └── test_cases.py
│   ├── [01;34mannotated_types-0.7.0.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   └── [01;34mlicenses[0m
│   │       └── LICENSE
│   ├── [01;34manyio[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── from_thread.cpython-312.pyc
│   │   │   ├── functools.cpython-312.pyc
│   │   │   ├── lowlevel.cpython-312.pyc
│   │   │   ├── pytest_plugin.cpython-312.pyc
│   │   │   ├── to_interpreter.cpython-312.pyc
│   │   │   ├── to_process.cpython-312.pyc
│   │   │   └── to_thread.cpython-312.pyc
│   │   ├── [01;34m_backends[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── _asyncio.cpython-312.pyc
│   │   │   │   └── _trio.cpython-312.pyc
│   │   │   ├── _asyncio.py
│   │   │   └── _trio.py
│   │   ├── [01;34m_core[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── _asyncio_selector_thread.cpython-312.pyc
│   │   │   │   ├── _contextmanagers.cpython-312.pyc
│   │   │   │   ├── _eventloop.cpython-312.pyc
│   │   │   │   ├── _exceptions.cpython-312.pyc
│   │   │   │   ├── _fileio.cpython-312.pyc
│   │   │   │   ├── _resources.cpython-312.pyc
│   │   │   │   ├── _signals.cpython-312.pyc
│   │   │   │   ├── _sockets.cpython-312.pyc
│   │   │   │   ├── _streams.cpython-312.pyc
│   │   │   │   ├── _subprocesses.cpython-312.pyc
│   │   │   │   ├── _synchronization.cpython-312.pyc
│   │   │   │   ├── _tasks.cpython-312.pyc
│   │   │   │   ├── _tempfile.cpython-312.pyc
│   │   │   │   ├── _testing.cpython-312.pyc
│   │   │   │   └── _typedattr.cpython-312.pyc
│   │   │   ├── _asyncio_selector_thread.py
│   │   │   ├── _contextmanagers.py
│   │   │   ├── _eventloop.py
│   │   │   ├── _exceptions.py
│   │   │   ├── _fileio.py
│   │   │   ├── _resources.py
│   │   │   ├── _signals.py
│   │   │   ├── _sockets.py
│   │   │   ├── _streams.py
│   │   │   ├── _subprocesses.py
│   │   │   ├── _synchronization.py
│   │   │   ├── _tasks.py
│   │   │   ├── _tempfile.py
│   │   │   ├── _testing.py
│   │   │   └── _typedattr.py
│   │   ├── [01;34mabc[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── _eventloop.cpython-312.pyc
│   │   │   │   ├── _resources.cpython-312.pyc
│   │   │   │   ├── _sockets.cpython-312.pyc
│   │   │   │   ├── _streams.cpython-312.pyc
│   │   │   │   ├── _subprocesses.cpython-312.pyc
│   │   │   │   ├── _tasks.cpython-312.pyc
│   │   │   │   └── _testing.cpython-312.pyc
│   │   │   ├── _eventloop.py
│   │   │   ├── _resources.py
│   │   │   ├── _sockets.py
│   │   │   ├── _streams.py
│   │   │   ├── _subprocesses.py
│   │   │   ├── _tasks.py
│   │   │   └── _testing.py
│   │   ├── from_thread.py
│   │   ├── functools.py
│   │   ├── lowlevel.py
│   │   ├── py.typed
│   │   ├── pytest_plugin.py
│   │   ├── [01;34mstreams[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── buffered.cpython-312.pyc
│   │   │   │   ├── file.cpython-312.pyc
│   │   │   │   ├── memory.cpython-312.pyc
│   │   │   │   ├── stapled.cpython-312.pyc
│   │   │   │   ├── text.cpython-312.pyc
│   │   │   │   └── tls.cpython-312.pyc
│   │   │   ├── buffered.py
│   │   │   ├── file.py
│   │   │   ├── memory.py
│   │   │   ├── stapled.py
│   │   │   ├── text.py
│   │   │   └── tls.py
│   │   ├── to_interpreter.py
│   │   ├── to_process.py
│   │   └── to_thread.py
│   ├── [01;34manyio-4.12.1.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   ├── entry_points.txt
│   │   ├── [01;34mlicenses[0m
│   │   │   └── LICENSE
│   │   └── top_level.txt
│   ├── [01;34mapp[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── main.cpython-312.pyc
│   │   ├── [01;34mapi[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   └── __init__.cpython-312.pyc
│   │   │   └── [01;34mv1[0m
│   │   │       ├── [01;34m__pycache__[0m
│   │   │       │   ├── despatch.cpython-312.pyc
│   │   │       │   └── health.cpython-312.pyc
│   │   │       ├── despatch.py
│   │   │       └── health.py
│   │   ├── [01;34mcore[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   └── ubl_generator.cpython-312.pyc
│   │   │   ├── config.py
│   │   │   ├── ubl_generator.py
│   │   │   └── xml_validator.py
│   │   ├── [01;34mdata[0m
│   │   │   └── mock_orders.json
│   │   ├── main.py
│   │   ├── [01;34mmodels[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   └── despatch_models.cpython-312.pyc
│   │   │   └── despatch_models.py
│   │   ├── [01;34mtemplates[0m
│   │   │   └── despatch_advice_template.xml
│   │   └── [01;34mxsd[0m
│   │       ├── [01;34mcommon[0m
│   │       │   ├── CCTS_CCT_SchemaModule-2.1.xsd
│   │       │   ├── UBL-CommonAggregateComponents-2.1.xsd
│   │       │   ├── UBL-CommonBasicComponents-2.1.xsd
│   │       │   ├── UBL-CommonExtensionComponents-2.1.xsd
│   │       │   ├── UBL-CommonSignatureComponents-2.1.xsd
│   │       │   ├── UBL-CoreComponentParameters-2.1.xsd
│   │       │   ├── UBL-ExtensionContentDataType-2.1.xsd
│   │       │   ├── UBL-QualifiedDataTypes-2.1.xsd
│   │       │   ├── UBL-SignatureAggregateComponents-2.1.xsd
│   │       │   ├── UBL-SignatureBasicComponents-2.1.xsd
│   │       │   ├── UBL-UnqualifiedDataTypes-2.1.xsd
│   │       │   ├── UBL-XAdESv132-2.1.xsd
│   │       │   ├── UBL-XAdESv141-2.1.xsd
│   │       │   └── UBL-xmldsig-core-schema-2.1.xsd
│   │       └── [01;34mmaindoc[0m
│   │           ├── UBL-ApplicationResponse-2.1.xsd
│   │           ├── UBL-AttachedDocument-2.1.xsd
│   │           ├── UBL-AwardedNotification-2.1.xsd
│   │           ├── UBL-BillOfLading-2.1.xsd
│   │           ├── UBL-CallForTenders-2.1.xsd
│   │           ├── UBL-Catalogue-2.1.xsd
│   │           ├── UBL-CatalogueDeletion-2.1.xsd
│   │           ├── UBL-CatalogueItemSpecificationUpdate-2.1.xsd
│   │           ├── UBL-CataloguePricingUpdate-2.1.xsd
│   │           ├── UBL-CatalogueRequest-2.1.xsd
│   │           ├── UBL-CertificateOfOrigin-2.1.xsd
│   │           ├── UBL-ContractAwardNotice-2.1.xsd
│   │           ├── UBL-ContractNotice-2.1.xsd
│   │           ├── UBL-CreditNote-2.1.xsd
│   │           ├── UBL-DebitNote-2.1.xsd
│   │           ├── UBL-DespatchAdvice-2.1.xsd
│   │           ├── UBL-DocumentStatus-2.1.xsd
│   │           ├── UBL-DocumentStatusRequest-2.1.xsd
│   │           ├── UBL-ExceptionCriteria-2.1.xsd
│   │           ├── UBL-ExceptionNotification-2.1.xsd
│   │           ├── UBL-Forecast-2.1.xsd
│   │           ├── UBL-ForecastRevision-2.1.xsd
│   │           ├── UBL-ForwardingInstructions-2.1.xsd
│   │           ├── UBL-FreightInvoice-2.1.xsd
│   │           ├── UBL-FulfilmentCancellation-2.1.xsd
│   │           ├── UBL-GoodsItemItinerary-2.1.xsd
│   │           ├── UBL-GuaranteeCertificate-2.1.xsd
│   │           ├── UBL-InstructionForReturns-2.1.xsd
│   │           ├── UBL-InventoryReport-2.1.xsd
│   │           ├── UBL-Invoice-2.1.xsd
│   │           ├── UBL-ItemInformationRequest-2.1.xsd
│   │           ├── UBL-Order-2.1.xsd
│   │           ├── UBL-OrderCancellation-2.1.xsd
│   │           ├── UBL-OrderChange-2.1.xsd
│   │           ├── UBL-OrderResponse-2.1.xsd
│   │           ├── UBL-OrderResponseSimple-2.1.xsd
│   │           ├── UBL-PackingList-2.1.xsd
│   │           ├── UBL-PriorInformationNotice-2.1.xsd
│   │           ├── UBL-ProductActivity-2.1.xsd
│   │           ├── UBL-Quotation-2.1.xsd
│   │           ├── UBL-ReceiptAdvice-2.1.xsd
│   │           ├── UBL-Reminder-2.1.xsd
│   │           ├── UBL-RemittanceAdvice-2.1.xsd
│   │           ├── UBL-RequestForQuotation-2.1.xsd
│   │           ├── UBL-RetailEvent-2.1.xsd
│   │           ├── UBL-SelfBilledCreditNote-2.1.xsd
│   │           ├── UBL-SelfBilledInvoice-2.1.xsd
│   │           ├── UBL-Statement-2.1.xsd
│   │           ├── UBL-StockAvailabilityReport-2.1.xsd
│   │           ├── UBL-Tender-2.1.xsd
│   │           ├── UBL-TenderReceipt-2.1.xsd
│   │           ├── UBL-TendererQualification-2.1.xsd
│   │           ├── UBL-TendererQualificationResponse-2.1.xsd
│   │           ├── UBL-TradeItemLocationProfile-2.1.xsd
│   │           ├── UBL-TransportExecutionPlan-2.1.xsd
│   │           ├── UBL-TransportExecutionPlanRequest-2.1.xsd
│   │           ├── UBL-TransportProgressStatus-2.1.xsd
│   │           ├── UBL-TransportProgressStatusRequest-2.1.xsd
│   │           ├── UBL-TransportServiceDescription-2.1.xsd
│   │           ├── UBL-TransportServiceDescriptionRequest-2.1.xsd
│   │           ├── UBL-TransportationStatus-2.1.xsd
│   │           ├── UBL-TransportationStatusRequest-2.1.xsd
│   │           ├── UBL-UnawardedNotification-2.1.xsd
│   │           ├── UBL-UtilityStatement-2.1.xsd
│   │           └── UBL-Waybill-2.1.xsd
│   ├── [01;34mbin[0m
│   │   ├── [01;32mdotenv[0m
│   │   ├── [01;32memail_validator[0m
│   │   ├── [01;32mfastapi[0m
│   │   ├── [01;32mpy.test[0m
│   │   ├── [01;32mpygmentize[0m
│   │   ├── [01;32mpytest[0m
│   │   ├── [01;32muvicorn[0m
│   │   ├── [01;32mxmlschema-json2xml[0m
│   │   ├── [01;32mxmlschema-validate[0m
│   │   └── [01;32mxmlschema-xml2json[0m
│   ├── [01;34mclick[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── _compat.cpython-312.pyc
│   │   │   ├── _termui_impl.cpython-312.pyc
│   │   │   ├── _textwrap.cpython-312.pyc
│   │   │   ├── _utils.cpython-312.pyc
│   │   │   ├── _winconsole.cpython-312.pyc
│   │   │   ├── core.cpython-312.pyc
│   │   │   ├── decorators.cpython-312.pyc
│   │   │   ├── exceptions.cpython-312.pyc
│   │   │   ├── formatting.cpython-312.pyc
│   │   │   ├── globals.cpython-312.pyc
│   │   │   ├── parser.cpython-312.pyc
│   │   │   ├── shell_completion.cpython-312.pyc
│   │   │   ├── termui.cpython-312.pyc
│   │   │   ├── testing.cpython-312.pyc
│   │   │   ├── types.cpython-312.pyc
│   │   │   └── utils.cpython-312.pyc
│   │   ├── _compat.py
│   │   ├── _termui_impl.py
│   │   ├── _textwrap.py
│   │   ├── _utils.py
│   │   ├── _winconsole.py
│   │   ├── core.py
│   │   ├── decorators.py
│   │   ├── exceptions.py
│   │   ├── formatting.py
│   │   ├── globals.py
│   │   ├── parser.py
│   │   ├── py.typed
│   │   ├── shell_completion.py
│   │   ├── termui.py
│   │   ├── testing.py
│   │   ├── types.py
│   │   └── utils.py
│   ├── [01;34mclick-8.3.1.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   └── [01;34mlicenses[0m
│   │       └── LICENSE.txt
│   ├── [01;34mdns[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── _asyncbackend.cpython-312.pyc
│   │   │   ├── _asyncio_backend.cpython-312.pyc
│   │   │   ├── _ddr.cpython-312.pyc
│   │   │   ├── _features.cpython-312.pyc
│   │   │   ├── _immutable_ctx.cpython-312.pyc
│   │   │   ├── _no_ssl.cpython-312.pyc
│   │   │   ├── _tls_util.cpython-312.pyc
│   │   │   ├── _trio_backend.cpython-312.pyc
│   │   │   ├── asyncbackend.cpython-312.pyc
│   │   │   ├── asyncquery.cpython-312.pyc
│   │   │   ├── asyncresolver.cpython-312.pyc
│   │   │   ├── btree.cpython-312.pyc
│   │   │   ├── btreezone.cpython-312.pyc
│   │   │   ├── dnssec.cpython-312.pyc
│   │   │   ├── dnssectypes.cpython-312.pyc
│   │   │   ├── e164.cpython-312.pyc
│   │   │   ├── edns.cpython-312.pyc
│   │   │   ├── entropy.cpython-312.pyc
│   │   │   ├── enum.cpython-312.pyc
│   │   │   ├── exception.cpython-312.pyc
│   │   │   ├── flags.cpython-312.pyc
│   │   │   ├── grange.cpython-312.pyc
│   │   │   ├── immutable.cpython-312.pyc
│   │   │   ├── inet.cpython-312.pyc
│   │   │   ├── ipv4.cpython-312.pyc
│   │   │   ├── ipv6.cpython-312.pyc
│   │   │   ├── message.cpython-312.pyc
│   │   │   ├── name.cpython-312.pyc
│   │   │   ├── namedict.cpython-312.pyc
│   │   │   ├── nameserver.cpython-312.pyc
│   │   │   ├── node.cpython-312.pyc
│   │   │   ├── opcode.cpython-312.pyc
│   │   │   ├── query.cpython-312.pyc
│   │   │   ├── rcode.cpython-312.pyc
│   │   │   ├── rdata.cpython-312.pyc
│   │   │   ├── rdataclass.cpython-312.pyc
│   │   │   ├── rdataset.cpython-312.pyc
│   │   │   ├── rdatatype.cpython-312.pyc
│   │   │   ├── renderer.cpython-312.pyc
│   │   │   ├── resolver.cpython-312.pyc
│   │   │   ├── reversename.cpython-312.pyc
│   │   │   ├── rrset.cpython-312.pyc
│   │   │   ├── serial.cpython-312.pyc
│   │   │   ├── set.cpython-312.pyc
│   │   │   ├── tokenizer.cpython-312.pyc
│   │   │   ├── transaction.cpython-312.pyc
│   │   │   ├── tsig.cpython-312.pyc
│   │   │   ├── tsigkeyring.cpython-312.pyc
│   │   │   ├── ttl.cpython-312.pyc
│   │   │   ├── update.cpython-312.pyc
│   │   │   ├── version.cpython-312.pyc
│   │   │   ├── versioned.cpython-312.pyc
│   │   │   ├── win32util.cpython-312.pyc
│   │   │   ├── wire.cpython-312.pyc
│   │   │   ├── xfr.cpython-312.pyc
│   │   │   ├── zone.cpython-312.pyc
│   │   │   ├── zonefile.cpython-312.pyc
│   │   │   └── zonetypes.cpython-312.pyc
│   │   ├── _asyncbackend.py
│   │   ├── _asyncio_backend.py
│   │   ├── _ddr.py
│   │   ├── _features.py
│   │   ├── _immutable_ctx.py
│   │   ├── _no_ssl.py
│   │   ├── _tls_util.py
│   │   ├── _trio_backend.py
│   │   ├── asyncbackend.py
│   │   ├── asyncquery.py
│   │   ├── asyncresolver.py
│   │   ├── btree.py
│   │   ├── btreezone.py
│   │   ├── dnssec.py
│   │   ├── [01;34mdnssecalgs[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── base.cpython-312.pyc
│   │   │   │   ├── cryptography.cpython-312.pyc
│   │   │   │   ├── dsa.cpython-312.pyc
│   │   │   │   ├── ecdsa.cpython-312.pyc
│   │   │   │   ├── eddsa.cpython-312.pyc
│   │   │   │   └── rsa.cpython-312.pyc
│   │   │   ├── base.py
│   │   │   ├── cryptography.py
│   │   │   ├── dsa.py
│   │   │   ├── ecdsa.py
│   │   │   ├── eddsa.py
│   │   │   └── rsa.py
│   │   ├── dnssectypes.py
│   │   ├── e164.py
│   │   ├── edns.py
│   │   ├── entropy.py
│   │   ├── enum.py
│   │   ├── exception.py
│   │   ├── flags.py
│   │   ├── grange.py
│   │   ├── immutable.py
│   │   ├── inet.py
│   │   ├── ipv4.py
│   │   ├── ipv6.py
│   │   ├── message.py
│   │   ├── name.py
│   │   ├── namedict.py
│   │   ├── nameserver.py
│   │   ├── node.py
│   │   ├── opcode.py
│   │   ├── py.typed
│   │   ├── query.py
│   │   ├── [01;34mquic[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── _asyncio.cpython-312.pyc
│   │   │   │   ├── _common.cpython-312.pyc
│   │   │   │   ├── _sync.cpython-312.pyc
│   │   │   │   └── _trio.cpython-312.pyc
│   │   │   ├── _asyncio.py
│   │   │   ├── _common.py
│   │   │   ├── _sync.py
│   │   │   └── _trio.py
│   │   ├── rcode.py
│   │   ├── rdata.py
│   │   ├── rdataclass.py
│   │   ├── rdataset.py
│   │   ├── rdatatype.py
│   │   ├── [01;34mrdtypes[0m
│   │   │   ├── [01;34mANY[0m
│   │   │   │   ├── AFSDB.py
│   │   │   │   ├── AMTRELAY.py
│   │   │   │   ├── AVC.py
│   │   │   │   ├── CAA.py
│   │   │   │   ├── CDNSKEY.py
│   │   │   │   ├── CDS.py
│   │   │   │   ├── CERT.py
│   │   │   │   ├── CNAME.py
│   │   │   │   ├── CSYNC.py
│   │   │   │   ├── DLV.py
│   │   │   │   ├── DNAME.py
│   │   │   │   ├── DNSKEY.py
│   │   │   │   ├── DS.py
│   │   │   │   ├── DSYNC.py
│   │   │   │   ├── EUI48.py
│   │   │   │   ├── EUI64.py
│   │   │   │   ├── GPOS.py
│   │   │   │   ├── HINFO.py
│   │   │   │   ├── HIP.py
│   │   │   │   ├── ISDN.py
│   │   │   │   ├── L32.py
│   │   │   │   ├── L64.py
│   │   │   │   ├── LOC.py
│   │   │   │   ├── LP.py
│   │   │   │   ├── MX.py
│   │   │   │   ├── NID.py
│   │   │   │   ├── NINFO.py
│   │   │   │   ├── NS.py
│   │   │   │   ├── NSEC.py
│   │   │   │   ├── NSEC3.py
│   │   │   │   ├── NSEC3PARAM.py
│   │   │   │   ├── OPENPGPKEY.py
│   │   │   │   ├── OPT.py
│   │   │   │   ├── PTR.py
│   │   │   │   ├── RESINFO.py
│   │   │   │   ├── RP.py
│   │   │   │   ├── RRSIG.py
│   │   │   │   ├── RT.py
│   │   │   │   ├── SMIMEA.py
│   │   │   │   ├── SOA.py
│   │   │   │   ├── SPF.py
│   │   │   │   ├── SSHFP.py
│   │   │   │   ├── TKEY.py
│   │   │   │   ├── TLSA.py
│   │   │   │   ├── TSIG.py
│   │   │   │   ├── TXT.py
│   │   │   │   ├── URI.py
│   │   │   │   ├── WALLET.py
│   │   │   │   ├── X25.py
│   │   │   │   ├── ZONEMD.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── [01;34m__pycache__[0m
│   │   │   │       ├── AFSDB.cpython-312.pyc
│   │   │   │       ├── AMTRELAY.cpython-312.pyc
│   │   │   │       ├── AVC.cpython-312.pyc
│   │   │   │       ├── CAA.cpython-312.pyc
│   │   │   │       ├── CDNSKEY.cpython-312.pyc
│   │   │   │       ├── CDS.cpython-312.pyc
│   │   │   │       ├── CERT.cpython-312.pyc
│   │   │   │       ├── CNAME.cpython-312.pyc
│   │   │   │       ├── CSYNC.cpython-312.pyc
│   │   │   │       ├── DLV.cpython-312.pyc
│   │   │   │       ├── DNAME.cpython-312.pyc
│   │   │   │       ├── DNSKEY.cpython-312.pyc
│   │   │   │       ├── DS.cpython-312.pyc
│   │   │   │       ├── DSYNC.cpython-312.pyc
│   │   │   │       ├── EUI48.cpython-312.pyc
│   │   │   │       ├── EUI64.cpython-312.pyc
│   │   │   │       ├── GPOS.cpython-312.pyc
│   │   │   │       ├── HINFO.cpython-312.pyc
│   │   │   │       ├── HIP.cpython-312.pyc
│   │   │   │       ├── ISDN.cpython-312.pyc
│   │   │   │       ├── L32.cpython-312.pyc
│   │   │   │       ├── L64.cpython-312.pyc
│   │   │   │       ├── LOC.cpython-312.pyc
│   │   │   │       ├── LP.cpython-312.pyc
│   │   │   │       ├── MX.cpython-312.pyc
│   │   │   │       ├── NID.cpython-312.pyc
│   │   │   │       ├── NINFO.cpython-312.pyc
│   │   │   │       ├── NS.cpython-312.pyc
│   │   │   │       ├── NSEC.cpython-312.pyc
│   │   │   │       ├── NSEC3.cpython-312.pyc
│   │   │   │       ├── NSEC3PARAM.cpython-312.pyc
│   │   │   │       ├── OPENPGPKEY.cpython-312.pyc
│   │   │   │       ├── OPT.cpython-312.pyc
│   │   │   │       ├── PTR.cpython-312.pyc
│   │   │   │       ├── RESINFO.cpython-312.pyc
│   │   │   │       ├── RP.cpython-312.pyc
│   │   │   │       ├── RRSIG.cpython-312.pyc
│   │   │   │       ├── RT.cpython-312.pyc
│   │   │   │       ├── SMIMEA.cpython-312.pyc
│   │   │   │       ├── SOA.cpython-312.pyc
│   │   │   │       ├── SPF.cpython-312.pyc
│   │   │   │       ├── SSHFP.cpython-312.pyc
│   │   │   │       ├── TKEY.cpython-312.pyc
│   │   │   │       ├── TLSA.cpython-312.pyc
│   │   │   │       ├── TSIG.cpython-312.pyc
│   │   │   │       ├── TXT.cpython-312.pyc
│   │   │   │       ├── URI.cpython-312.pyc
│   │   │   │       ├── WALLET.cpython-312.pyc
│   │   │   │       ├── X25.cpython-312.pyc
│   │   │   │       ├── ZONEMD.cpython-312.pyc
│   │   │   │       └── __init__.cpython-312.pyc
│   │   │   ├── [01;34mCH[0m
│   │   │   │   ├── A.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── [01;34m__pycache__[0m
│   │   │   │       ├── A.cpython-312.pyc
│   │   │   │       └── __init__.cpython-312.pyc
│   │   │   ├── [01;34mIN[0m
│   │   │   │   ├── A.py
│   │   │   │   ├── AAAA.py
│   │   │   │   ├── APL.py
│   │   │   │   ├── DHCID.py
│   │   │   │   ├── HTTPS.py
│   │   │   │   ├── IPSECKEY.py
│   │   │   │   ├── KX.py
│   │   │   │   ├── NAPTR.py
│   │   │   │   ├── NSAP.py
│   │   │   │   ├── NSAP_PTR.py
│   │   │   │   ├── PX.py
│   │   │   │   ├── SRV.py
│   │   │   │   ├── SVCB.py
│   │   │   │   ├── WKS.py
│   │   │   │   ├── __init__.py
│   │   │   │   └── [01;34m__pycache__[0m
│   │   │   │       ├── A.cpython-312.pyc
│   │   │   │       ├── AAAA.cpython-312.pyc
│   │   │   │       ├── APL.cpython-312.pyc
│   │   │   │       ├── DHCID.cpython-312.pyc
│   │   │   │       ├── HTTPS.cpython-312.pyc
│   │   │   │       ├── IPSECKEY.cpython-312.pyc
│   │   │   │       ├── KX.cpython-312.pyc
│   │   │   │       ├── NAPTR.cpython-312.pyc
│   │   │   │       ├── NSAP.cpython-312.pyc
│   │   │   │       ├── NSAP_PTR.cpython-312.pyc
│   │   │   │       ├── PX.cpython-312.pyc
│   │   │   │       ├── SRV.cpython-312.pyc
│   │   │   │       ├── SVCB.cpython-312.pyc
│   │   │   │       ├── WKS.cpython-312.pyc
│   │   │   │       └── __init__.cpython-312.pyc
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── dnskeybase.cpython-312.pyc
│   │   │   │   ├── dsbase.cpython-312.pyc
│   │   │   │   ├── euibase.cpython-312.pyc
│   │   │   │   ├── mxbase.cpython-312.pyc
│   │   │   │   ├── nsbase.cpython-312.pyc
│   │   │   │   ├── svcbbase.cpython-312.pyc
│   │   │   │   ├── tlsabase.cpython-312.pyc
│   │   │   │   ├── txtbase.cpython-312.pyc
│   │   │   │   └── util.cpython-312.pyc
│   │   │   ├── dnskeybase.py
│   │   │   ├── dsbase.py
│   │   │   ├── euibase.py
│   │   │   ├── mxbase.py
│   │   │   ├── nsbase.py
│   │   │   ├── svcbbase.py
│   │   │   ├── tlsabase.py
│   │   │   ├── txtbase.py
│   │   │   └── util.py
│   │   ├── renderer.py
│   │   ├── resolver.py
│   │   ├── reversename.py
│   │   ├── rrset.py
│   │   ├── serial.py
│   │   ├── set.py
│   │   ├── tokenizer.py
│   │   ├── transaction.py
│   │   ├── tsig.py
│   │   ├── tsigkeyring.py
│   │   ├── ttl.py
│   │   ├── update.py
│   │   ├── version.py
│   │   ├── versioned.py
│   │   ├── win32util.py
│   │   ├── wire.py
│   │   ├── xfr.py
│   │   ├── zone.py
│   │   ├── zonefile.py
│   │   └── zonetypes.py
│   ├── [01;34mdnspython-2.8.0.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   └── [01;34mlicenses[0m
│   │       └── LICENSE
│   ├── [01;34mdotenv[0m
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── __main__.cpython-312.pyc
│   │   │   ├── cli.cpython-312.pyc
│   │   │   ├── ipython.cpython-312.pyc
│   │   │   ├── main.cpython-312.pyc
│   │   │   ├── parser.cpython-312.pyc
│   │   │   ├── variables.cpython-312.pyc
│   │   │   └── version.cpython-312.pyc
│   │   ├── cli.py
│   │   ├── ipython.py
│   │   ├── main.py
│   │   ├── parser.py
│   │   ├── py.typed
│   │   ├── variables.py
│   │   └── version.py
│   ├── [01;34melementpath[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── _typing.cpython-312.pyc
│   │   │   ├── aliases.cpython-312.pyc
│   │   │   ├── collations.cpython-312.pyc
│   │   │   ├── compare.cpython-312.pyc
│   │   │   ├── decoder.cpython-312.pyc
│   │   │   ├── etree.cpython-312.pyc
│   │   │   ├── exceptions.cpython-312.pyc
│   │   │   ├── helpers.cpython-312.pyc
│   │   │   ├── namespaces.cpython-312.pyc
│   │   │   ├── protocols.cpython-312.pyc
│   │   │   ├── schema_proxy.cpython-312.pyc
│   │   │   ├── sequence_types.cpython-312.pyc
│   │   │   ├── serialization.cpython-312.pyc
│   │   │   ├── tdop.cpython-312.pyc
│   │   │   ├── tree_builders.cpython-312.pyc
│   │   │   ├── xpath3.cpython-312.pyc
│   │   │   ├── xpath_context.cpython-312.pyc
│   │   │   ├── xpath_nodes.cpython-312.pyc
│   │   │   ├── xpath_selectors.cpython-312.pyc
│   │   │   └── xpath_tokens.cpython-312.pyc
│   │   ├── _typing.py
│   │   ├── aliases.py
│   │   ├── collations.py
│   │   ├── compare.py
│   │   ├── [01;34mdatatypes[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── atomic_types.cpython-312.pyc
│   │   │   │   ├── binary.cpython-312.pyc
│   │   │   │   ├── datetime.cpython-312.pyc
│   │   │   │   ├── numeric.cpython-312.pyc
│   │   │   │   ├── proxies.cpython-312.pyc
│   │   │   │   ├── qname.cpython-312.pyc
│   │   │   │   ├── string.cpython-312.pyc
│   │   │   │   ├── untyped.cpython-312.pyc
│   │   │   │   └── uri.cpython-312.pyc
│   │   │   ├── atomic_types.py
│   │   │   ├── binary.py
│   │   │   ├── datetime.py
│   │   │   ├── numeric.py
│   │   │   ├── proxies.py
│   │   │   ├── qname.py
│   │   │   ├── string.py
│   │   │   ├── untyped.py
│   │   │   └── uri.py
│   │   ├── decoder.py
│   │   ├── etree.py
│   │   ├── exceptions.py
│   │   ├── helpers.py
│   │   ├── namespaces.py
│   │   ├── protocols.py
│   │   ├── py.typed
│   │   ├── [01;34mregex[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── character_classes.cpython-312.pyc
│   │   │   │   ├── codepoints.cpython-312.pyc
│   │   │   │   ├── patterns.cpython-312.pyc
│   │   │   │   ├── unicode_blocks.cpython-312.pyc
│   │   │   │   ├── unicode_categories.cpython-312.pyc
│   │   │   │   └── unicode_subsets.cpython-312.pyc
│   │   │   ├── character_classes.py
│   │   │   ├── codepoints.py
│   │   │   ├── patterns.py
│   │   │   ├── unicode_blocks.py
│   │   │   ├── unicode_categories.py
│   │   │   └── unicode_subsets.py
│   │   ├── schema_proxy.py
│   │   ├── sequence_types.py
│   │   ├── serialization.py
│   │   ├── tdop.py
│   │   ├── tree_builders.py
│   │   ├── [01;34mvalidators[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   └── __init__.cpython-312.pyc
│   │   │   ├── analyze-string.xsd
│   │   │   └── schema-for-json.xsd
│   │   ├── [01;34mxpath1[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── _xpath1_axes.cpython-312.pyc
│   │   │   │   ├── _xpath1_functions.cpython-312.pyc
│   │   │   │   ├── _xpath1_operators.cpython-312.pyc
│   │   │   │   └── xpath1_parser.cpython-312.pyc
│   │   │   ├── _xpath1_axes.py
│   │   │   ├── _xpath1_functions.py
│   │   │   ├── _xpath1_operators.py
│   │   │   └── xpath1_parser.py
│   │   ├── [01;34mxpath2[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── _xpath2_constructors.cpython-312.pyc
│   │   │   │   ├── _xpath2_functions.cpython-312.pyc
│   │   │   │   ├── _xpath2_operators.cpython-312.pyc
│   │   │   │   └── xpath2_parser.cpython-312.pyc
│   │   │   ├── _xpath2_constructors.py
│   │   │   ├── _xpath2_functions.py
│   │   │   ├── _xpath2_operators.py
│   │   │   └── xpath2_parser.py
│   │   ├── xpath3.py
│   │   ├── [01;34mxpath30[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── _translation_maps.cpython-312.pyc
│   │   │   │   ├── _xpath30_functions.cpython-312.pyc
│   │   │   │   ├── _xpath30_operators.cpython-312.pyc
│   │   │   │   ├── xpath30_helpers.cpython-312.pyc
│   │   │   │   └── xpath30_parser.cpython-312.pyc
│   │   │   ├── _translation_maps.py
│   │   │   ├── _xpath30_functions.py
│   │   │   ├── _xpath30_operators.py
│   │   │   ├── xpath30_helpers.py
│   │   │   └── xpath30_parser.py
│   │   ├── [01;34mxpath31[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── _xpath31_functions.cpython-312.pyc
│   │   │   │   ├── _xpath31_operators.cpython-312.pyc
│   │   │   │   └── xpath31_parser.cpython-312.pyc
│   │   │   ├── _xpath31_functions.py
│   │   │   ├── _xpath31_operators.py
│   │   │   └── xpath31_parser.py
│   │   ├── xpath_context.py
│   │   ├── xpath_nodes.py
│   │   ├── xpath_selectors.py
│   │   └── xpath_tokens.py
│   ├── [01;34melementpath-4.8.0.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── LICENSE
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   └── top_level.txt
│   ├── [01;34memail_validator[0m
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── __main__.cpython-312.pyc
│   │   │   ├── deliverability.cpython-312.pyc
│   │   │   ├── exceptions.cpython-312.pyc
│   │   │   ├── rfc_constants.cpython-312.pyc
│   │   │   ├── syntax.cpython-312.pyc
│   │   │   ├── types.cpython-312.pyc
│   │   │   ├── validate_email.cpython-312.pyc
│   │   │   └── version.cpython-312.pyc
│   │   ├── deliverability.py
│   │   ├── exceptions.py
│   │   ├── py.typed
│   │   ├── rfc_constants.py
│   │   ├── syntax.py
│   │   ├── types.py
│   │   ├── validate_email.py
│   │   └── version.py
│   ├── [01;34memail_validator-2.3.0.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── REQUESTED
│   │   ├── WHEEL
│   │   ├── entry_points.txt
│   │   ├── [01;34mlicenses[0m
│   │   │   └── LICENSE
│   │   └── top_level.txt
│   ├── [01;34mfastapi[0m
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── __main__.cpython-312.pyc
│   │   │   ├── applications.cpython-312.pyc
│   │   │   ├── background.cpython-312.pyc
│   │   │   ├── cli.cpython-312.pyc
│   │   │   ├── concurrency.cpython-312.pyc
│   │   │   ├── datastructures.cpython-312.pyc
│   │   │   ├── encoders.cpython-312.pyc
│   │   │   ├── exception_handlers.cpython-312.pyc
│   │   │   ├── exceptions.cpython-312.pyc
│   │   │   ├── logger.cpython-312.pyc
│   │   │   ├── param_functions.cpython-312.pyc
│   │   │   ├── params.cpython-312.pyc
│   │   │   ├── requests.cpython-312.pyc
│   │   │   ├── responses.cpython-312.pyc
│   │   │   ├── routing.cpython-312.pyc
│   │   │   ├── sse.cpython-312.pyc
│   │   │   ├── staticfiles.cpython-312.pyc
│   │   │   ├── templating.cpython-312.pyc
│   │   │   ├── testclient.cpython-312.pyc
│   │   │   ├── types.cpython-312.pyc
│   │   │   ├── utils.cpython-312.pyc
│   │   │   └── websockets.cpython-312.pyc
│   │   ├── [01;34m_compat[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── shared.cpython-312.pyc
│   │   │   │   └── v2.cpython-312.pyc
│   │   │   ├── shared.py
│   │   │   └── v2.py
│   │   ├── applications.py
│   │   ├── background.py
│   │   ├── cli.py
│   │   ├── concurrency.py
│   │   ├── datastructures.py
│   │   ├── [01;34mdependencies[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── models.cpython-312.pyc
│   │   │   │   └── utils.cpython-312.pyc
│   │   │   ├── models.py
│   │   │   └── utils.py
│   │   ├── encoders.py
│   │   ├── exception_handlers.py
│   │   ├── exceptions.py
│   │   ├── logger.py
│   │   ├── [01;34mmiddleware[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── asyncexitstack.cpython-312.pyc
│   │   │   │   ├── cors.cpython-312.pyc
│   │   │   │   ├── gzip.cpython-312.pyc
│   │   │   │   ├── httpsredirect.cpython-312.pyc
│   │   │   │   ├── trustedhost.cpython-312.pyc
│   │   │   │   └── wsgi.cpython-312.pyc
│   │   │   ├── asyncexitstack.py
│   │   │   ├── cors.py
│   │   │   ├── gzip.py
│   │   │   ├── httpsredirect.py
│   │   │   ├── trustedhost.py
│   │   │   └── wsgi.py
│   │   ├── [01;34mopenapi[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── constants.cpython-312.pyc
│   │   │   │   ├── docs.cpython-312.pyc
│   │   │   │   ├── models.cpython-312.pyc
│   │   │   │   └── utils.cpython-312.pyc
│   │   │   ├── constants.py
│   │   │   ├── docs.py
│   │   │   ├── models.py
│   │   │   └── utils.py
│   │   ├── param_functions.py
│   │   ├── params.py
│   │   ├── py.typed
│   │   ├── requests.py
│   │   ├── responses.py
│   │   ├── routing.py
│   │   ├── [01;34msecurity[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── api_key.cpython-312.pyc
│   │   │   │   ├── base.cpython-312.pyc
│   │   │   │   ├── http.cpython-312.pyc
│   │   │   │   ├── oauth2.cpython-312.pyc
│   │   │   │   ├── open_id_connect_url.cpython-312.pyc
│   │   │   │   └── utils.cpython-312.pyc
│   │   │   ├── api_key.py
│   │   │   ├── base.py
│   │   │   ├── http.py
│   │   │   ├── oauth2.py
│   │   │   ├── open_id_connect_url.py
│   │   │   └── utils.py
│   │   ├── sse.py
│   │   ├── staticfiles.py
│   │   ├── templating.py
│   │   ├── testclient.py
│   │   ├── types.py
│   │   ├── utils.py
│   │   └── websockets.py
│   ├── [01;34mfastapi-0.135.1.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── REQUESTED
│   │   ├── WHEEL
│   │   ├── entry_points.txt
│   │   └── [01;34mlicenses[0m
│   │       └── LICENSE
│   ├── [01;34mh11[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── _abnf.cpython-312.pyc
│   │   │   ├── _connection.cpython-312.pyc
│   │   │   ├── _events.cpython-312.pyc
│   │   │   ├── _headers.cpython-312.pyc
│   │   │   ├── _readers.cpython-312.pyc
│   │   │   ├── _receivebuffer.cpython-312.pyc
│   │   │   ├── _state.cpython-312.pyc
│   │   │   ├── _util.cpython-312.pyc
│   │   │   ├── _version.cpython-312.pyc
│   │   │   └── _writers.cpython-312.pyc
│   │   ├── _abnf.py
│   │   ├── _connection.py
│   │   ├── _events.py
│   │   ├── _headers.py
│   │   ├── _readers.py
│   │   ├── _receivebuffer.py
│   │   ├── _state.py
│   │   ├── _util.py
│   │   ├── _version.py
│   │   ├── _writers.py
│   │   └── py.typed
│   ├── [01;34mh11-0.16.0.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   ├── [01;34mlicenses[0m
│   │   │   └── LICENSE.txt
│   │   └── top_level.txt
│   ├── [01;34midna[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── codec.cpython-312.pyc
│   │   │   ├── compat.cpython-312.pyc
│   │   │   ├── core.cpython-312.pyc
│   │   │   ├── idnadata.cpython-312.pyc
│   │   │   ├── intranges.cpython-312.pyc
│   │   │   ├── package_data.cpython-312.pyc
│   │   │   └── uts46data.cpython-312.pyc
│   │   ├── codec.py
│   │   ├── compat.py
│   │   ├── core.py
│   │   ├── idnadata.py
│   │   ├── intranges.py
│   │   ├── package_data.py
│   │   ├── py.typed
│   │   └── uts46data.py
│   ├── [01;34midna-3.11.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   └── [01;34mlicenses[0m
│   │       └── LICENSE.md
│   ├── [01;34miniconfig[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── _parse.cpython-312.pyc
│   │   │   ├── _version.cpython-312.pyc
│   │   │   └── exceptions.cpython-312.pyc
│   │   ├── _parse.py
│   │   ├── _version.py
│   │   ├── exceptions.py
│   │   └── py.typed
│   ├── [01;34miniconfig-2.3.0.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   ├── [01;34mlicenses[0m
│   │   │   └── LICENSE
│   │   └── top_level.txt
│   ├── [01;34mjinja2[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── _identifier.cpython-312.pyc
│   │   │   ├── async_utils.cpython-312.pyc
│   │   │   ├── bccache.cpython-312.pyc
│   │   │   ├── compiler.cpython-312.pyc
│   │   │   ├── constants.cpython-312.pyc
│   │   │   ├── debug.cpython-312.pyc
│   │   │   ├── defaults.cpython-312.pyc
│   │   │   ├── environment.cpython-312.pyc
│   │   │   ├── exceptions.cpython-312.pyc
│   │   │   ├── ext.cpython-312.pyc
│   │   │   ├── filters.cpython-312.pyc
│   │   │   ├── idtracking.cpython-312.pyc
│   │   │   ├── lexer.cpython-312.pyc
│   │   │   ├── loaders.cpython-312.pyc
│   │   │   ├── meta.cpython-312.pyc
│   │   │   ├── nativetypes.cpython-312.pyc
│   │   │   ├── nodes.cpython-312.pyc
│   │   │   ├── optimizer.cpython-312.pyc
│   │   │   ├── parser.cpython-312.pyc
│   │   │   ├── runtime.cpython-312.pyc
│   │   │   ├── sandbox.cpython-312.pyc
│   │   │   ├── tests.cpython-312.pyc
│   │   │   ├── utils.cpython-312.pyc
│   │   │   └── visitor.cpython-312.pyc
│   │   ├── _identifier.py
│   │   ├── async_utils.py
│   │   ├── bccache.py
│   │   ├── compiler.py
│   │   ├── constants.py
│   │   ├── debug.py
│   │   ├── defaults.py
│   │   ├── environment.py
│   │   ├── exceptions.py
│   │   ├── ext.py
│   │   ├── filters.py
│   │   ├── idtracking.py
│   │   ├── lexer.py
│   │   ├── loaders.py
│   │   ├── meta.py
│   │   ├── nativetypes.py
│   │   ├── nodes.py
│   │   ├── optimizer.py
│   │   ├── parser.py
│   │   ├── py.typed
│   │   ├── runtime.py
│   │   ├── sandbox.py
│   │   ├── tests.py
│   │   ├── utils.py
│   │   └── visitor.py
│   ├── [01;34mjinja2-3.1.6.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── REQUESTED
│   │   ├── WHEEL
│   │   ├── entry_points.txt
│   │   └── [01;34mlicenses[0m
│   │       └── LICENSE.txt
│   ├── [01;34mlxml[0m
│   │   ├── ElementInclude.py
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── ElementInclude.cpython-312.pyc
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── _elementpath.cpython-312.pyc
│   │   │   ├── builder.cpython-312.pyc
│   │   │   ├── cssselect.cpython-312.pyc
│   │   │   ├── doctestcompare.cpython-312.pyc
│   │   │   ├── pyclasslookup.cpython-312.pyc
│   │   │   ├── sax.cpython-312.pyc
│   │   │   └── usedoctest.cpython-312.pyc
│   │   ├── [01;32m_elementpath.cpython-312-x86_64-linux-gnu.so[0m
│   │   ├── _elementpath.py
│   │   ├── apihelpers.pxi
│   │   ├── [01;32mbuilder.cpython-312-x86_64-linux-gnu.so[0m
│   │   ├── builder.py
│   │   ├── classlookup.pxi
│   │   ├── cleanup.pxi
│   │   ├── cssselect.py
│   │   ├── debug.pxi
│   │   ├── docloader.pxi
│   │   ├── doctestcompare.py
│   │   ├── dtd.pxi
│   │   ├── [01;32metree.cpython-312-x86_64-linux-gnu.so[0m
│   │   ├── etree.h
│   │   ├── etree.pyx
│   │   ├── etree_api.h
│   │   ├── extensions.pxi
│   │   ├── [01;34mhtml[0m
│   │   │   ├── ElementSoup.py
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── ElementSoup.cpython-312.pyc
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── _diffcommand.cpython-312.pyc
│   │   │   │   ├── _html5builder.cpython-312.pyc
│   │   │   │   ├── _setmixin.cpython-312.pyc
│   │   │   │   ├── builder.cpython-312.pyc
│   │   │   │   ├── clean.cpython-312.pyc
│   │   │   │   ├── defs.cpython-312.pyc
│   │   │   │   ├── diff.cpython-312.pyc
│   │   │   │   ├── formfill.cpython-312.pyc
│   │   │   │   ├── html5parser.cpython-312.pyc
│   │   │   │   ├── soupparser.cpython-312.pyc
│   │   │   │   └── usedoctest.cpython-312.pyc
│   │   │   ├── _diffcommand.py
│   │   │   ├── _html5builder.py
│   │   │   ├── _setmixin.py
│   │   │   ├── builder.py
│   │   │   ├── clean.py
│   │   │   ├── defs.py
│   │   │   ├── [01;32mdiff.cpython-312-x86_64-linux-gnu.so[0m
│   │   │   ├── diff.py
│   │   │   ├── formfill.py
│   │   │   ├── html5parser.py
│   │   │   ├── soupparser.py
│   │   │   └── usedoctest.py
│   │   ├── [01;34mincludes[0m
│   │   │   ├── __init__.pxd
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   └── __init__.cpython-312.pyc
│   │   │   ├── c14n.pxd
│   │   │   ├── config.pxd
│   │   │   ├── dtdvalid.pxd
│   │   │   ├── etree_defs.h
│   │   │   ├── etreepublic.pxd
│   │   │   ├── [01;34mextlibs[0m
│   │   │   │   ├── __init__.py
│   │   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   │   └── __init__.cpython-312.pyc
│   │   │   │   ├── libcharset.h
│   │   │   │   ├── localcharset.h
│   │   │   │   ├── zconf.h
│   │   │   │   └── zlib.h
│   │   │   ├── htmlparser.pxd
│   │   │   ├── [01;34mlibexslt[0m
│   │   │   │   ├── __init__.py
│   │   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   │   └── __init__.cpython-312.pyc
│   │   │   │   ├── exslt.h
│   │   │   │   ├── exsltconfig.h
│   │   │   │   └── exsltexports.h
│   │   │   ├── [01;34mlibxml[0m
│   │   │   │   ├── HTMLparser.h
│   │   │   │   ├── HTMLtree.h
│   │   │   │   ├── SAX.h
│   │   │   │   ├── SAX2.h
│   │   │   │   ├── __init__.py
│   │   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   │   └── __init__.cpython-312.pyc
│   │   │   │   ├── c14n.h
│   │   │   │   ├── catalog.h
│   │   │   │   ├── chvalid.h
│   │   │   │   ├── debugXML.h
│   │   │   │   ├── dict.h
│   │   │   │   ├── encoding.h
│   │   │   │   ├── entities.h
│   │   │   │   ├── globals.h
│   │   │   │   ├── hash.h
│   │   │   │   ├── list.h
│   │   │   │   ├── nanoftp.h
│   │   │   │   ├── nanohttp.h
│   │   │   │   ├── parser.h
│   │   │   │   ├── parserInternals.h
│   │   │   │   ├── relaxng.h
│   │   │   │   ├── schemasInternals.h
│   │   │   │   ├── schematron.h
│   │   │   │   ├── threads.h
│   │   │   │   ├── tree.h
│   │   │   │   ├── uri.h
│   │   │   │   ├── valid.h
│   │   │   │   ├── xinclude.h
│   │   │   │   ├── xlink.h
│   │   │   │   ├── xmlIO.h
│   │   │   │   ├── xmlautomata.h
│   │   │   │   ├── xmlerror.h
│   │   │   │   ├── xmlexports.h
│   │   │   │   ├── xmlmemory.h
│   │   │   │   ├── xmlmodule.h
│   │   │   │   ├── xmlreader.h
│   │   │   │   ├── xmlregexp.h
│   │   │   │   ├── xmlsave.h
│   │   │   │   ├── xmlschemas.h
│   │   │   │   ├── xmlschemastypes.h
│   │   │   │   ├── xmlstring.h
│   │   │   │   ├── xmlunicode.h
│   │   │   │   ├── xmlversion.h
│   │   │   │   ├── xmlwriter.h
│   │   │   │   ├── xpath.h
│   │   │   │   ├── xpathInternals.h
│   │   │   │   └── xpointer.h
│   │   │   ├── [01;34mlibxslt[0m
│   │   │   │   ├── __init__.py
│   │   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   │   └── __init__.cpython-312.pyc
│   │   │   │   ├── attributes.h
│   │   │   │   ├── documents.h
│   │   │   │   ├── extensions.h
│   │   │   │   ├── extra.h
│   │   │   │   ├── functions.h
│   │   │   │   ├── imports.h
│   │   │   │   ├── keys.h
│   │   │   │   ├── namespaces.h
│   │   │   │   ├── numbersInternals.h
│   │   │   │   ├── pattern.h
│   │   │   │   ├── preproc.h
│   │   │   │   ├── security.h
│   │   │   │   ├── templates.h
│   │   │   │   ├── transform.h
│   │   │   │   ├── variables.h
│   │   │   │   ├── xslt.h
│   │   │   │   ├── xsltInternals.h
│   │   │   │   ├── xsltconfig.h
│   │   │   │   ├── xsltexports.h
│   │   │   │   ├── xsltlocale.h
│   │   │   │   └── xsltutils.h
│   │   │   ├── lxml-version.h
│   │   │   ├── relaxng.pxd
│   │   │   ├── schematron.pxd
│   │   │   ├── tree.pxd
│   │   │   ├── uri.pxd
│   │   │   ├── xinclude.pxd
│   │   │   ├── xmlerror.pxd
│   │   │   ├── xmlparser.pxd
│   │   │   ├── xmlschema.pxd
│   │   │   ├── xpath.pxd
│   │   │   └── xslt.pxd
│   │   ├── [01;34misoschematron[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   └── __init__.cpython-312.pyc
│   │   │   └── [01;34mresources[0m
│   │   │       ├── [01;34mrng[0m
│   │   │       │   └── iso-schematron.rng
│   │   │       └── [01;34mxsl[0m
│   │   │           ├── RNG2Schtrn.xsl
│   │   │           ├── XSD2Schtrn.xsl
│   │   │           └── [01;34miso-schematron-xslt1[0m
│   │   │               ├── iso_abstract_expand.xsl
│   │   │               ├── iso_dsdl_include.xsl
│   │   │               ├── iso_schematron_message.xsl
│   │   │               ├── iso_schematron_skeleton_for_xslt1.xsl
│   │   │               ├── iso_svrl_for_xslt1.xsl
│   │   │               └── readme.txt
│   │   ├── iterparse.pxi
│   │   ├── lxml.etree.h
│   │   ├── lxml.etree_api.h
│   │   ├── nsclasses.pxi
│   │   ├── [01;32mobjectify.cpython-312-x86_64-linux-gnu.so[0m
│   │   ├── objectify.pyx
│   │   ├── objectpath.pxi
│   │   ├── parser.pxi
│   │   ├── parsertarget.pxi
│   │   ├── proxy.pxi
│   │   ├── public-api.pxi
│   │   ├── pyclasslookup.py
│   │   ├── readonlytree.pxi
│   │   ├── relaxng.pxi
│   │   ├── [01;32msax.cpython-312-x86_64-linux-gnu.so[0m
│   │   ├── sax.py
│   │   ├── saxparser.pxi
│   │   ├── schematron.pxi
│   │   ├── serializer.pxi
│   │   ├── usedoctest.py
│   │   ├── xinclude.pxi
│   │   ├── xmlerror.pxi
│   │   ├── xmlid.pxi
│   │   ├── xmlschema.pxi
│   │   ├── xpath.pxi
│   │   ├── xslt.pxi
│   │   └── xsltext.pxi
│   ├── [01;34mlxml-5.3.0.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── LICENSE.txt
│   │   ├── LICENSES.txt
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── REQUESTED
│   │   ├── WHEEL
│   │   └── top_level.txt
│   ├── [01;34mmangum[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── adapter.cpython-312.pyc
│   │   │   ├── exceptions.cpython-312.pyc
│   │   │   └── types.cpython-312.pyc
│   │   ├── adapter.py
│   │   ├── exceptions.py
│   │   ├── [01;34mhandlers[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── alb.cpython-312.pyc
│   │   │   │   ├── api_gateway.cpython-312.pyc
│   │   │   │   ├── lambda_at_edge.cpython-312.pyc
│   │   │   │   └── utils.cpython-312.pyc
│   │   │   ├── alb.py
│   │   │   ├── api_gateway.py
│   │   │   ├── lambda_at_edge.py
│   │   │   └── utils.py
│   │   ├── [01;34mprotocols[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── http.cpython-312.pyc
│   │   │   │   └── lifespan.cpython-312.pyc
│   │   │   ├── http.py
│   │   │   └── lifespan.py
│   │   ├── py.typed
│   │   └── types.py
│   ├── [01;34mmangum-0.21.0.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── REQUESTED
│   │   ├── WHEEL
│   │   └── [01;34mlicenses[0m
│   │       └── LICENSE
│   ├── [01;34mmarkupsafe[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── _native.cpython-312.pyc
│   │   ├── _native.py
│   │   ├── _speedups.c
│   │   ├── [01;32m_speedups.cpython-312-x86_64-linux-gnu.so[0m
│   │   ├── _speedups.pyi
│   │   └── py.typed
│   ├── [01;34mmarkupsafe-3.0.3.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   ├── [01;34mlicenses[0m
│   │   │   └── LICENSE.txt
│   │   └── top_level.txt
│   ├── [01;34mmultipart[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── decoders.cpython-312.pyc
│   │   │   ├── exceptions.cpython-312.pyc
│   │   │   └── multipart.cpython-312.pyc
│   │   ├── decoders.py
│   │   ├── exceptions.py
│   │   └── multipart.py
│   ├── [01;34mpackaging[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── _elffile.cpython-312.pyc
│   │   │   ├── _manylinux.cpython-312.pyc
│   │   │   ├── _musllinux.cpython-312.pyc
│   │   │   ├── _parser.cpython-312.pyc
│   │   │   ├── _structures.cpython-312.pyc
│   │   │   ├── _tokenizer.cpython-312.pyc
│   │   │   ├── markers.cpython-312.pyc
│   │   │   ├── metadata.cpython-312.pyc
│   │   │   ├── pylock.cpython-312.pyc
│   │   │   ├── requirements.cpython-312.pyc
│   │   │   ├── specifiers.cpython-312.pyc
│   │   │   ├── tags.cpython-312.pyc
│   │   │   ├── utils.cpython-312.pyc
│   │   │   └── version.cpython-312.pyc
│   │   ├── _elffile.py
│   │   ├── _manylinux.py
│   │   ├── _musllinux.py
│   │   ├── _parser.py
│   │   ├── _structures.py
│   │   ├── _tokenizer.py
│   │   ├── [01;34mlicenses[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   └── _spdx.cpython-312.pyc
│   │   │   └── _spdx.py
│   │   ├── markers.py
│   │   ├── metadata.py
│   │   ├── py.typed
│   │   ├── pylock.py
│   │   ├── requirements.py
│   │   ├── specifiers.py
│   │   ├── tags.py
│   │   ├── utils.py
│   │   └── version.py
│   ├── [01;34mpackaging-26.0.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   └── [01;34mlicenses[0m
│   │       ├── LICENSE
│   │       ├── LICENSE.APACHE
│   │       └── LICENSE.BSD
│   ├── [01;34mpluggy[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── _callers.cpython-312.pyc
│   │   │   ├── _hooks.cpython-312.pyc
│   │   │   ├── _manager.cpython-312.pyc
│   │   │   ├── _result.cpython-312.pyc
│   │   │   ├── _tracing.cpython-312.pyc
│   │   │   ├── _version.cpython-312.pyc
│   │   │   └── _warnings.cpython-312.pyc
│   │   ├── _callers.py
│   │   ├── _hooks.py
│   │   ├── _manager.py
│   │   ├── _result.py
│   │   ├── _tracing.py
│   │   ├── _version.py
│   │   ├── _warnings.py
│   │   └── py.typed
│   ├── [01;34mpluggy-1.6.0.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   ├── [01;34mlicenses[0m
│   │   │   └── LICENSE
│   │   └── top_level.txt
│   ├── py.py
│   ├── [01;34mpydantic[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── _migration.cpython-312.pyc
│   │   │   ├── alias_generators.cpython-312.pyc
│   │   │   ├── aliases.cpython-312.pyc
│   │   │   ├── annotated_handlers.cpython-312.pyc
│   │   │   ├── class_validators.cpython-312.pyc
│   │   │   ├── color.cpython-312.pyc
│   │   │   ├── config.cpython-312.pyc
│   │   │   ├── dataclasses.cpython-312.pyc
│   │   │   ├── datetime_parse.cpython-312.pyc
│   │   │   ├── decorator.cpython-312.pyc
│   │   │   ├── env_settings.cpython-312.pyc
│   │   │   ├── error_wrappers.cpython-312.pyc
│   │   │   ├── errors.cpython-312.pyc
│   │   │   ├── fields.cpython-312.pyc
│   │   │   ├── functional_serializers.cpython-312.pyc
│   │   │   ├── functional_validators.cpython-312.pyc
│   │   │   ├── generics.cpython-312.pyc
│   │   │   ├── json.cpython-312.pyc
│   │   │   ├── json_schema.cpython-312.pyc
│   │   │   ├── main.cpython-312.pyc
│   │   │   ├── mypy.cpython-312.pyc
│   │   │   ├── networks.cpython-312.pyc
│   │   │   ├── parse.cpython-312.pyc
│   │   │   ├── root_model.cpython-312.pyc
│   │   │   ├── schema.cpython-312.pyc
│   │   │   ├── tools.cpython-312.pyc
│   │   │   ├── type_adapter.cpython-312.pyc
│   │   │   ├── types.cpython-312.pyc
│   │   │   ├── typing.cpython-312.pyc
│   │   │   ├── utils.cpython-312.pyc
│   │   │   ├── validate_call_decorator.cpython-312.pyc
│   │   │   ├── validators.cpython-312.pyc
│   │   │   ├── version.cpython-312.pyc
│   │   │   └── warnings.cpython-312.pyc
│   │   ├── [01;34m_internal[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── _config.cpython-312.pyc
│   │   │   │   ├── _core_metadata.cpython-312.pyc
│   │   │   │   ├── _core_utils.cpython-312.pyc
│   │   │   │   ├── _dataclasses.cpython-312.pyc
│   │   │   │   ├── _decorators.cpython-312.pyc
│   │   │   │   ├── _decorators_v1.cpython-312.pyc
│   │   │   │   ├── _discriminated_union.cpython-312.pyc
│   │   │   │   ├── _docs_extraction.cpython-312.pyc
│   │   │   │   ├── _fields.cpython-312.pyc
│   │   │   │   ├── _forward_ref.cpython-312.pyc
│   │   │   │   ├── _generate_schema.cpython-312.pyc
│   │   │   │   ├── _generics.cpython-312.pyc
│   │   │   │   ├── _git.cpython-312.pyc
│   │   │   │   ├── _import_utils.cpython-312.pyc
│   │   │   │   ├── _internal_dataclass.cpython-312.pyc
│   │   │   │   ├── _known_annotated_metadata.cpython-312.pyc
│   │   │   │   ├── _mock_val_ser.cpython-312.pyc
│   │   │   │   ├── _model_construction.cpython-312.pyc
│   │   │   │   ├── _namespace_utils.cpython-312.pyc
│   │   │   │   ├── _repr.cpython-312.pyc
│   │   │   │   ├── _schema_gather.cpython-312.pyc
│   │   │   │   ├── _schema_generation_shared.cpython-312.pyc
│   │   │   │   ├── _serializers.cpython-312.pyc
│   │   │   │   ├── _signature.cpython-312.pyc
│   │   │   │   ├── _typing_extra.cpython-312.pyc
│   │   │   │   ├── _utils.cpython-312.pyc
│   │   │   │   ├── _validate_call.cpython-312.pyc
│   │   │   │   └── _validators.cpython-312.pyc
│   │   │   ├── _config.py
│   │   │   ├── _core_metadata.py
│   │   │   ├── _core_utils.py
│   │   │   ├── _dataclasses.py
│   │   │   ├── _decorators.py
│   │   │   ├── _decorators_v1.py
│   │   │   ├── _discriminated_union.py
│   │   │   ├── _docs_extraction.py
│   │   │   ├── _fields.py
│   │   │   ├── _forward_ref.py
│   │   │   ├── _generate_schema.py
│   │   │   ├── _generics.py
│   │   │   ├── _git.py
│   │   │   ├── _import_utils.py
│   │   │   ├── _internal_dataclass.py
│   │   │   ├── _known_annotated_metadata.py
│   │   │   ├── _mock_val_ser.py
│   │   │   ├── _model_construction.py
│   │   │   ├── _namespace_utils.py
│   │   │   ├── _repr.py
│   │   │   ├── _schema_gather.py
│   │   │   ├── _schema_generation_shared.py
│   │   │   ├── _serializers.py
│   │   │   ├── _signature.py
│   │   │   ├── _typing_extra.py
│   │   │   ├── _utils.py
│   │   │   ├── _validate_call.py
│   │   │   └── _validators.py
│   │   ├── _migration.py
│   │   ├── alias_generators.py
│   │   ├── aliases.py
│   │   ├── annotated_handlers.py
│   │   ├── class_validators.py
│   │   ├── color.py
│   │   ├── config.py
│   │   ├── dataclasses.py
│   │   ├── datetime_parse.py
│   │   ├── decorator.py
│   │   ├── [01;34mdeprecated[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── class_validators.cpython-312.pyc
│   │   │   │   ├── config.cpython-312.pyc
│   │   │   │   ├── copy_internals.cpython-312.pyc
│   │   │   │   ├── decorator.cpython-312.pyc
│   │   │   │   ├── json.cpython-312.pyc
│   │   │   │   ├── parse.cpython-312.pyc
│   │   │   │   └── tools.cpython-312.pyc
│   │   │   ├── class_validators.py
│   │   │   ├── config.py
│   │   │   ├── copy_internals.py
│   │   │   ├── decorator.py
│   │   │   ├── json.py
│   │   │   ├── parse.py
│   │   │   └── tools.py
│   │   ├── env_settings.py
│   │   ├── error_wrappers.py
│   │   ├── errors.py
│   │   ├── [01;34mexperimental[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── arguments_schema.cpython-312.pyc
│   │   │   │   ├── missing_sentinel.cpython-312.pyc
│   │   │   │   └── pipeline.cpython-312.pyc
│   │   │   ├── arguments_schema.py
│   │   │   ├── missing_sentinel.py
│   │   │   └── pipeline.py
│   │   ├── fields.py
│   │   ├── functional_serializers.py
│   │   ├── functional_validators.py
│   │   ├── generics.py
│   │   ├── json.py
│   │   ├── json_schema.py
│   │   ├── main.py
│   │   ├── mypy.py
│   │   ├── networks.py
│   │   ├── parse.py
│   │   ├── [01;34mplugin[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── _loader.cpython-312.pyc
│   │   │   │   └── _schema_validator.cpython-312.pyc
│   │   │   ├── _loader.py
│   │   │   └── _schema_validator.py
│   │   ├── py.typed
│   │   ├── root_model.py
│   │   ├── schema.py
│   │   ├── tools.py
│   │   ├── type_adapter.py
│   │   ├── types.py
│   │   ├── typing.py
│   │   ├── utils.py
│   │   ├── [01;34mv1[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── _hypothesis_plugin.cpython-312.pyc
│   │   │   │   ├── annotated_types.cpython-312.pyc
│   │   │   │   ├── class_validators.cpython-312.pyc
│   │   │   │   ├── color.cpython-312.pyc
│   │   │   │   ├── config.cpython-312.pyc
│   │   │   │   ├── dataclasses.cpython-312.pyc
│   │   │   │   ├── datetime_parse.cpython-312.pyc
│   │   │   │   ├── decorator.cpython-312.pyc
│   │   │   │   ├── env_settings.cpython-312.pyc
│   │   │   │   ├── error_wrappers.cpython-312.pyc
│   │   │   │   ├── errors.cpython-312.pyc
│   │   │   │   ├── fields.cpython-312.pyc
│   │   │   │   ├── generics.cpython-312.pyc
│   │   │   │   ├── json.cpython-312.pyc
│   │   │   │   ├── main.cpython-312.pyc
│   │   │   │   ├── mypy.cpython-312.pyc
│   │   │   │   ├── networks.cpython-312.pyc
│   │   │   │   ├── parse.cpython-312.pyc
│   │   │   │   ├── schema.cpython-312.pyc
│   │   │   │   ├── tools.cpython-312.pyc
│   │   │   │   ├── types.cpython-312.pyc
│   │   │   │   ├── typing.cpython-312.pyc
│   │   │   │   ├── utils.cpython-312.pyc
│   │   │   │   ├── validators.cpython-312.pyc
│   │   │   │   └── version.cpython-312.pyc
│   │   │   ├── _hypothesis_plugin.py
│   │   │   ├── annotated_types.py
│   │   │   ├── class_validators.py
│   │   │   ├── color.py
│   │   │   ├── config.py
│   │   │   ├── dataclasses.py
│   │   │   ├── datetime_parse.py
│   │   │   ├── decorator.py
│   │   │   ├── env_settings.py
│   │   │   ├── error_wrappers.py
│   │   │   ├── errors.py
│   │   │   ├── fields.py
│   │   │   ├── generics.py
│   │   │   ├── json.py
│   │   │   ├── main.py
│   │   │   ├── mypy.py
│   │   │   ├── networks.py
│   │   │   ├── parse.py
│   │   │   ├── py.typed
│   │   │   ├── schema.py
│   │   │   ├── tools.py
│   │   │   ├── types.py
│   │   │   ├── typing.py
│   │   │   ├── utils.py
│   │   │   ├── validators.py
│   │   │   └── version.py
│   │   ├── validate_call_decorator.py
│   │   ├── validators.py
│   │   ├── version.py
│   │   └── warnings.py
│   ├── [01;34mpydantic-2.12.5.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── REQUESTED
│   │   ├── WHEEL
│   │   └── [01;34mlicenses[0m
│   │       └── LICENSE
│   ├── [01;34mpydantic_core[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── core_schema.cpython-312.pyc
│   │   ├── [01;32m_pydantic_core.cpython-312-x86_64-linux-gnu.so[0m
│   │   ├── _pydantic_core.pyi
│   │   ├── core_schema.py
│   │   └── py.typed
│   ├── [01;34mpydantic_core-2.41.5.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   └── [01;34mlicenses[0m
│   │       └── LICENSE
│   ├── [01;34mpygments[0m
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── __main__.cpython-312.pyc
│   │   │   ├── cmdline.cpython-312.pyc
│   │   │   ├── console.cpython-312.pyc
│   │   │   ├── filter.cpython-312.pyc
│   │   │   ├── formatter.cpython-312.pyc
│   │   │   ├── lexer.cpython-312.pyc
│   │   │   ├── modeline.cpython-312.pyc
│   │   │   ├── plugin.cpython-312.pyc
│   │   │   ├── regexopt.cpython-312.pyc
│   │   │   ├── scanner.cpython-312.pyc
│   │   │   ├── sphinxext.cpython-312.pyc
│   │   │   ├── style.cpython-312.pyc
│   │   │   ├── token.cpython-312.pyc
│   │   │   ├── unistring.cpython-312.pyc
│   │   │   └── util.cpython-312.pyc
│   │   ├── cmdline.py
│   │   ├── console.py
│   │   ├── filter.py
│   │   ├── [01;34mfilters[0m
│   │   │   ├── __init__.py
│   │   │   └── [01;34m__pycache__[0m
│   │   │       └── __init__.cpython-312.pyc
│   │   ├── formatter.py
│   │   ├── [01;34mformatters[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── _mapping.cpython-312.pyc
│   │   │   │   ├── bbcode.cpython-312.pyc
│   │   │   │   ├── groff.cpython-312.pyc
│   │   │   │   ├── html.cpython-312.pyc
│   │   │   │   ├── img.cpython-312.pyc
│   │   │   │   ├── irc.cpython-312.pyc
│   │   │   │   ├── latex.cpython-312.pyc
│   │   │   │   ├── other.cpython-312.pyc
│   │   │   │   ├── pangomarkup.cpython-312.pyc
│   │   │   │   ├── rtf.cpython-312.pyc
│   │   │   │   ├── svg.cpython-312.pyc
│   │   │   │   ├── terminal.cpython-312.pyc
│   │   │   │   └── terminal256.cpython-312.pyc
│   │   │   ├── _mapping.py
│   │   │   ├── bbcode.py
│   │   │   ├── groff.py
│   │   │   ├── html.py
│   │   │   ├── img.py
│   │   │   ├── irc.py
│   │   │   ├── latex.py
│   │   │   ├── other.py
│   │   │   ├── pangomarkup.py
│   │   │   ├── rtf.py
│   │   │   ├── svg.py
│   │   │   ├── terminal.py
│   │   │   └── terminal256.py
│   │   ├── lexer.py
│   │   ├── [01;34mlexers[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── _ada_builtins.cpython-312.pyc
│   │   │   │   ├── _asy_builtins.cpython-312.pyc
│   │   │   │   ├── _cl_builtins.cpython-312.pyc
│   │   │   │   ├── _cocoa_builtins.cpython-312.pyc
│   │   │   │   ├── _csound_builtins.cpython-312.pyc
│   │   │   │   ├── _css_builtins.cpython-312.pyc
│   │   │   │   ├── _googlesql_builtins.cpython-312.pyc
│   │   │   │   ├── _julia_builtins.cpython-312.pyc
│   │   │   │   ├── _lasso_builtins.cpython-312.pyc
│   │   │   │   ├── _lilypond_builtins.cpython-312.pyc
│   │   │   │   ├── _lua_builtins.cpython-312.pyc
│   │   │   │   ├── _luau_builtins.cpython-312.pyc
│   │   │   │   ├── _mapping.cpython-312.pyc
│   │   │   │   ├── _mql_builtins.cpython-312.pyc
│   │   │   │   ├── _mysql_builtins.cpython-312.pyc
│   │   │   │   ├── _openedge_builtins.cpython-312.pyc
│   │   │   │   ├── _php_builtins.cpython-312.pyc
│   │   │   │   ├── _postgres_builtins.cpython-312.pyc
│   │   │   │   ├── _qlik_builtins.cpython-312.pyc
│   │   │   │   ├── _scheme_builtins.cpython-312.pyc
│   │   │   │   ├── _scilab_builtins.cpython-312.pyc
│   │   │   │   ├── _sourcemod_builtins.cpython-312.pyc
│   │   │   │   ├── _sql_builtins.cpython-312.pyc
│   │   │   │   ├── _stan_builtins.cpython-312.pyc
│   │   │   │   ├── _stata_builtins.cpython-312.pyc
│   │   │   │   ├── _tsql_builtins.cpython-312.pyc
│   │   │   │   ├── _usd_builtins.cpython-312.pyc
│   │   │   │   ├── _vbscript_builtins.cpython-312.pyc
│   │   │   │   ├── _vim_builtins.cpython-312.pyc
│   │   │   │   ├── actionscript.cpython-312.pyc
│   │   │   │   ├── ada.cpython-312.pyc
│   │   │   │   ├── agile.cpython-312.pyc
│   │   │   │   ├── algebra.cpython-312.pyc
│   │   │   │   ├── ambient.cpython-312.pyc
│   │   │   │   ├── amdgpu.cpython-312.pyc
│   │   │   │   ├── ampl.cpython-312.pyc
│   │   │   │   ├── apdlexer.cpython-312.pyc
│   │   │   │   ├── apl.cpython-312.pyc
│   │   │   │   ├── archetype.cpython-312.pyc
│   │   │   │   ├── arrow.cpython-312.pyc
│   │   │   │   ├── arturo.cpython-312.pyc
│   │   │   │   ├── asc.cpython-312.pyc
│   │   │   │   ├── asm.cpython-312.pyc
│   │   │   │   ├── asn1.cpython-312.pyc
│   │   │   │   ├── automation.cpython-312.pyc
│   │   │   │   ├── bare.cpython-312.pyc
│   │   │   │   ├── basic.cpython-312.pyc
│   │   │   │   ├── bdd.cpython-312.pyc
│   │   │   │   ├── berry.cpython-312.pyc
│   │   │   │   ├── bibtex.cpython-312.pyc
│   │   │   │   ├── blueprint.cpython-312.pyc
│   │   │   │   ├── boa.cpython-312.pyc
│   │   │   │   ├── bqn.cpython-312.pyc
│   │   │   │   ├── business.cpython-312.pyc
│   │   │   │   ├── c_cpp.cpython-312.pyc
│   │   │   │   ├── c_like.cpython-312.pyc
│   │   │   │   ├── capnproto.cpython-312.pyc
│   │   │   │   ├── carbon.cpython-312.pyc
│   │   │   │   ├── cddl.cpython-312.pyc
│   │   │   │   ├── chapel.cpython-312.pyc
│   │   │   │   ├── clean.cpython-312.pyc
│   │   │   │   ├── codeql.cpython-312.pyc
│   │   │   │   ├── comal.cpython-312.pyc
│   │   │   │   ├── compiled.cpython-312.pyc
│   │   │   │   ├── configs.cpython-312.pyc
│   │   │   │   ├── console.cpython-312.pyc
│   │   │   │   ├── cplint.cpython-312.pyc
│   │   │   │   ├── crystal.cpython-312.pyc
│   │   │   │   ├── csound.cpython-312.pyc
│   │   │   │   ├── css.cpython-312.pyc
│   │   │   │   ├── d.cpython-312.pyc
│   │   │   │   ├── dalvik.cpython-312.pyc
│   │   │   │   ├── data.cpython-312.pyc
│   │   │   │   ├── dax.cpython-312.pyc
│   │   │   │   ├── devicetree.cpython-312.pyc
│   │   │   │   ├── diff.cpython-312.pyc
│   │   │   │   ├── dns.cpython-312.pyc
│   │   │   │   ├── dotnet.cpython-312.pyc
│   │   │   │   ├── dsls.cpython-312.pyc
│   │   │   │   ├── dylan.cpython-312.pyc
│   │   │   │   ├── ecl.cpython-312.pyc
│   │   │   │   ├── eiffel.cpython-312.pyc
│   │   │   │   ├── elm.cpython-312.pyc
│   │   │   │   ├── elpi.cpython-312.pyc
│   │   │   │   ├── email.cpython-312.pyc
│   │   │   │   ├── erlang.cpython-312.pyc
│   │   │   │   ├── esoteric.cpython-312.pyc
│   │   │   │   ├── ezhil.cpython-312.pyc
│   │   │   │   ├── factor.cpython-312.pyc
│   │   │   │   ├── fantom.cpython-312.pyc
│   │   │   │   ├── felix.cpython-312.pyc
│   │   │   │   ├── fift.cpython-312.pyc
│   │   │   │   ├── floscript.cpython-312.pyc
│   │   │   │   ├── forth.cpython-312.pyc
│   │   │   │   ├── fortran.cpython-312.pyc
│   │   │   │   ├── foxpro.cpython-312.pyc
│   │   │   │   ├── freefem.cpython-312.pyc
│   │   │   │   ├── func.cpython-312.pyc
│   │   │   │   ├── functional.cpython-312.pyc
│   │   │   │   ├── futhark.cpython-312.pyc
│   │   │   │   ├── gcodelexer.cpython-312.pyc
│   │   │   │   ├── gdscript.cpython-312.pyc
│   │   │   │   ├── gleam.cpython-312.pyc
│   │   │   │   ├── go.cpython-312.pyc
│   │   │   │   ├── grammar_notation.cpython-312.pyc
│   │   │   │   ├── graph.cpython-312.pyc
│   │   │   │   ├── graphics.cpython-312.pyc
│   │   │   │   ├── graphql.cpython-312.pyc
│   │   │   │   ├── graphviz.cpython-312.pyc
│   │   │   │   ├── gsql.cpython-312.pyc
│   │   │   │   ├── hare.cpython-312.pyc
│   │   │   │   ├── haskell.cpython-312.pyc
│   │   │   │   ├── haxe.cpython-312.pyc
│   │   │   │   ├── hdl.cpython-312.pyc
│   │   │   │   ├── hexdump.cpython-312.pyc
│   │   │   │   ├── html.cpython-312.pyc
│   │   │   │   ├── idl.cpython-312.pyc
│   │   │   │   ├── igor.cpython-312.pyc
│   │   │   │   ├── inferno.cpython-312.pyc
│   │   │   │   ├── installers.cpython-312.pyc
│   │   │   │   ├── int_fiction.cpython-312.pyc
│   │   │   │   ├── iolang.cpython-312.pyc
│   │   │   │   ├── j.cpython-312.pyc
│   │   │   │   ├── javascript.cpython-312.pyc
│   │   │   │   ├── jmespath.cpython-312.pyc
│   │   │   │   ├── jslt.cpython-312.pyc
│   │   │   │   ├── json5.cpython-312.pyc
│   │   │   │   ├── jsonnet.cpython-312.pyc
│   │   │   │   ├── jsx.cpython-312.pyc
│   │   │   │   ├── julia.cpython-312.pyc
│   │   │   │   ├── jvm.cpython-312.pyc
│   │   │   │   ├── kuin.cpython-312.pyc
│   │   │   │   ├── kusto.cpython-312.pyc
│   │   │   │   ├── ldap.cpython-312.pyc
│   │   │   │   ├── lean.cpython-312.pyc
│   │   │   │   ├── lilypond.cpython-312.pyc
│   │   │   │   ├── lisp.cpython-312.pyc
│   │   │   │   ├── macaulay2.cpython-312.pyc
│   │   │   │   ├── make.cpython-312.pyc
│   │   │   │   ├── maple.cpython-312.pyc
│   │   │   │   ├── markup.cpython-312.pyc
│   │   │   │   ├── math.cpython-312.pyc
│   │   │   │   ├── matlab.cpython-312.pyc
│   │   │   │   ├── maxima.cpython-312.pyc
│   │   │   │   ├── meson.cpython-312.pyc
│   │   │   │   ├── mime.cpython-312.pyc
│   │   │   │   ├── minecraft.cpython-312.pyc
│   │   │   │   ├── mips.cpython-312.pyc
│   │   │   │   ├── ml.cpython-312.pyc
│   │   │   │   ├── modeling.cpython-312.pyc
│   │   │   │   ├── modula2.cpython-312.pyc
│   │   │   │   ├── mojo.cpython-312.pyc
│   │   │   │   ├── monte.cpython-312.pyc
│   │   │   │   ├── mosel.cpython-312.pyc
│   │   │   │   ├── ncl.cpython-312.pyc
│   │   │   │   ├── nimrod.cpython-312.pyc
│   │   │   │   ├── nit.cpython-312.pyc
│   │   │   │   ├── nix.cpython-312.pyc
│   │   │   │   ├── numbair.cpython-312.pyc
│   │   │   │   ├── oberon.cpython-312.pyc
│   │   │   │   ├── objective.cpython-312.pyc
│   │   │   │   ├── ooc.cpython-312.pyc
│   │   │   │   ├── openscad.cpython-312.pyc
│   │   │   │   ├── other.cpython-312.pyc
│   │   │   │   ├── parasail.cpython-312.pyc
│   │   │   │   ├── parsers.cpython-312.pyc
│   │   │   │   ├── pascal.cpython-312.pyc
│   │   │   │   ├── pawn.cpython-312.pyc
│   │   │   │   ├── pddl.cpython-312.pyc
│   │   │   │   ├── perl.cpython-312.pyc
│   │   │   │   ├── phix.cpython-312.pyc
│   │   │   │   ├── php.cpython-312.pyc
│   │   │   │   ├── pointless.cpython-312.pyc
│   │   │   │   ├── pony.cpython-312.pyc
│   │   │   │   ├── praat.cpython-312.pyc
│   │   │   │   ├── procfile.cpython-312.pyc
│   │   │   │   ├── prolog.cpython-312.pyc
│   │   │   │   ├── promql.cpython-312.pyc
│   │   │   │   ├── prql.cpython-312.pyc
│   │   │   │   ├── ptx.cpython-312.pyc
│   │   │   │   ├── python.cpython-312.pyc
│   │   │   │   ├── q.cpython-312.pyc
│   │   │   │   ├── qlik.cpython-312.pyc
│   │   │   │   ├── qvt.cpython-312.pyc
│   │   │   │   ├── r.cpython-312.pyc
│   │   │   │   ├── rdf.cpython-312.pyc
│   │   │   │   ├── rebol.cpython-312.pyc
│   │   │   │   ├── rego.cpython-312.pyc
│   │   │   │   ├── resource.cpython-312.pyc
│   │   │   │   ├── ride.cpython-312.pyc
│   │   │   │   ├── rita.cpython-312.pyc
│   │   │   │   ├── rnc.cpython-312.pyc
│   │   │   │   ├── roboconf.cpython-312.pyc
│   │   │   │   ├── robotframework.cpython-312.pyc
│   │   │   │   ├── ruby.cpython-312.pyc
│   │   │   │   ├── rust.cpython-312.pyc
│   │   │   │   ├── sas.cpython-312.pyc
│   │   │   │   ├── savi.cpython-312.pyc
│   │   │   │   ├── scdoc.cpython-312.pyc
│   │   │   │   ├── scripting.cpython-312.pyc
│   │   │   │   ├── sgf.cpython-312.pyc
│   │   │   │   ├── shell.cpython-312.pyc
│   │   │   │   ├── sieve.cpython-312.pyc
│   │   │   │   ├── slash.cpython-312.pyc
│   │   │   │   ├── smalltalk.cpython-312.pyc
│   │   │   │   ├── smithy.cpython-312.pyc
│   │   │   │   ├── smv.cpython-312.pyc
│   │   │   │   ├── snobol.cpython-312.pyc
│   │   │   │   ├── solidity.cpython-312.pyc
│   │   │   │   ├── soong.cpython-312.pyc
│   │   │   │   ├── sophia.cpython-312.pyc
│   │   │   │   ├── special.cpython-312.pyc
│   │   │   │   ├── spice.cpython-312.pyc
│   │   │   │   ├── sql.cpython-312.pyc
│   │   │   │   ├── srcinfo.cpython-312.pyc
│   │   │   │   ├── stata.cpython-312.pyc
│   │   │   │   ├── supercollider.cpython-312.pyc
│   │   │   │   ├── tablegen.cpython-312.pyc
│   │   │   │   ├── tact.cpython-312.pyc
│   │   │   │   ├── tal.cpython-312.pyc
│   │   │   │   ├── tcl.cpython-312.pyc
│   │   │   │   ├── teal.cpython-312.pyc
│   │   │   │   ├── templates.cpython-312.pyc
│   │   │   │   ├── teraterm.cpython-312.pyc
│   │   │   │   ├── testing.cpython-312.pyc
│   │   │   │   ├── text.cpython-312.pyc
│   │   │   │   ├── textedit.cpython-312.pyc
│   │   │   │   ├── textfmts.cpython-312.pyc
│   │   │   │   ├── theorem.cpython-312.pyc
│   │   │   │   ├── thingsdb.cpython-312.pyc
│   │   │   │   ├── tlb.cpython-312.pyc
│   │   │   │   ├── tls.cpython-312.pyc
│   │   │   │   ├── tnt.cpython-312.pyc
│   │   │   │   ├── trafficscript.cpython-312.pyc
│   │   │   │   ├── typoscript.cpython-312.pyc
│   │   │   │   ├── typst.cpython-312.pyc
│   │   │   │   ├── ul4.cpython-312.pyc
│   │   │   │   ├── unicon.cpython-312.pyc
│   │   │   │   ├── urbi.cpython-312.pyc
│   │   │   │   ├── usd.cpython-312.pyc
│   │   │   │   ├── varnish.cpython-312.pyc
│   │   │   │   ├── verification.cpython-312.pyc
│   │   │   │   ├── verifpal.cpython-312.pyc
│   │   │   │   ├── vip.cpython-312.pyc
│   │   │   │   ├── vyper.cpython-312.pyc
│   │   │   │   ├── web.cpython-312.pyc
│   │   │   │   ├── webassembly.cpython-312.pyc
│   │   │   │   ├── webidl.cpython-312.pyc
│   │   │   │   ├── webmisc.cpython-312.pyc
│   │   │   │   ├── wgsl.cpython-312.pyc
│   │   │   │   ├── whiley.cpython-312.pyc
│   │   │   │   ├── wowtoc.cpython-312.pyc
│   │   │   │   ├── wren.cpython-312.pyc
│   │   │   │   ├── x10.cpython-312.pyc
│   │   │   │   ├── xorg.cpython-312.pyc
│   │   │   │   ├── yang.cpython-312.pyc
│   │   │   │   ├── yara.cpython-312.pyc
│   │   │   │   └── zig.cpython-312.pyc
│   │   │   ├── _ada_builtins.py
│   │   │   ├── _asy_builtins.py
│   │   │   ├── _cl_builtins.py
│   │   │   ├── _cocoa_builtins.py
│   │   │   ├── _csound_builtins.py
│   │   │   ├── _css_builtins.py
│   │   │   ├── _googlesql_builtins.py
│   │   │   ├── _julia_builtins.py
│   │   │   ├── _lasso_builtins.py
│   │   │   ├── _lilypond_builtins.py
│   │   │   ├── _lua_builtins.py
│   │   │   ├── _luau_builtins.py
│   │   │   ├── _mapping.py
│   │   │   ├── _mql_builtins.py
│   │   │   ├── _mysql_builtins.py
│   │   │   ├── _openedge_builtins.py
│   │   │   ├── _php_builtins.py
│   │   │   ├── _postgres_builtins.py
│   │   │   ├── _qlik_builtins.py
│   │   │   ├── _scheme_builtins.py
│   │   │   ├── _scilab_builtins.py
│   │   │   ├── _sourcemod_builtins.py
│   │   │   ├── _sql_builtins.py
│   │   │   ├── _stan_builtins.py
│   │   │   ├── _stata_builtins.py
│   │   │   ├── _tsql_builtins.py
│   │   │   ├── _usd_builtins.py
│   │   │   ├── _vbscript_builtins.py
│   │   │   ├── _vim_builtins.py
│   │   │   ├── actionscript.py
│   │   │   ├── ada.py
│   │   │   ├── agile.py
│   │   │   ├── algebra.py
│   │   │   ├── ambient.py
│   │   │   ├── amdgpu.py
│   │   │   ├── ampl.py
│   │   │   ├── apdlexer.py
│   │   │   ├── apl.py
│   │   │   ├── archetype.py
│   │   │   ├── arrow.py
│   │   │   ├── arturo.py
│   │   │   ├── asc.py
│   │   │   ├── asm.py
│   │   │   ├── asn1.py
│   │   │   ├── automation.py
│   │   │   ├── bare.py
│   │   │   ├── basic.py
│   │   │   ├── bdd.py
│   │   │   ├── berry.py
│   │   │   ├── bibtex.py
│   │   │   ├── blueprint.py
│   │   │   ├── boa.py
│   │   │   ├── bqn.py
│   │   │   ├── business.py
│   │   │   ├── c_cpp.py
│   │   │   ├── c_like.py
│   │   │   ├── capnproto.py
│   │   │   ├── carbon.py
│   │   │   ├── cddl.py
│   │   │   ├── chapel.py
│   │   │   ├── clean.py
│   │   │   ├── codeql.py
│   │   │   ├── comal.py
│   │   │   ├── compiled.py
│   │   │   ├── configs.py
│   │   │   ├── console.py
│   │   │   ├── cplint.py
│   │   │   ├── crystal.py
│   │   │   ├── csound.py
│   │   │   ├── css.py
│   │   │   ├── d.py
│   │   │   ├── dalvik.py
│   │   │   ├── data.py
│   │   │   ├── dax.py
│   │   │   ├── devicetree.py
│   │   │   ├── diff.py
│   │   │   ├── dns.py
│   │   │   ├── dotnet.py
│   │   │   ├── dsls.py
│   │   │   ├── dylan.py
│   │   │   ├── ecl.py
│   │   │   ├── eiffel.py
│   │   │   ├── elm.py
│   │   │   ├── elpi.py
│   │   │   ├── email.py
│   │   │   ├── erlang.py
│   │   │   ├── esoteric.py
│   │   │   ├── ezhil.py
│   │   │   ├── factor.py
│   │   │   ├── fantom.py
│   │   │   ├── felix.py
│   │   │   ├── fift.py
│   │   │   ├── floscript.py
│   │   │   ├── forth.py
│   │   │   ├── fortran.py
│   │   │   ├── foxpro.py
│   │   │   ├── freefem.py
│   │   │   ├── func.py
│   │   │   ├── functional.py
│   │   │   ├── futhark.py
│   │   │   ├── gcodelexer.py
│   │   │   ├── gdscript.py
│   │   │   ├── gleam.py
│   │   │   ├── go.py
│   │   │   ├── grammar_notation.py
│   │   │   ├── graph.py
│   │   │   ├── graphics.py
│   │   │   ├── graphql.py
│   │   │   ├── graphviz.py
│   │   │   ├── gsql.py
│   │   │   ├── hare.py
│   │   │   ├── haskell.py
│   │   │   ├── haxe.py
│   │   │   ├── hdl.py
│   │   │   ├── hexdump.py
│   │   │   ├── html.py
│   │   │   ├── idl.py
│   │   │   ├── igor.py
│   │   │   ├── inferno.py
│   │   │   ├── installers.py
│   │   │   ├── int_fiction.py
│   │   │   ├── iolang.py
│   │   │   ├── j.py
│   │   │   ├── javascript.py
│   │   │   ├── jmespath.py
│   │   │   ├── jslt.py
│   │   │   ├── json5.py
│   │   │   ├── jsonnet.py
│   │   │   ├── jsx.py
│   │   │   ├── julia.py
│   │   │   ├── jvm.py
│   │   │   ├── kuin.py
│   │   │   ├── kusto.py
│   │   │   ├── ldap.py
│   │   │   ├── lean.py
│   │   │   ├── lilypond.py
│   │   │   ├── lisp.py
│   │   │   ├── macaulay2.py
│   │   │   ├── make.py
│   │   │   ├── maple.py
│   │   │   ├── markup.py
│   │   │   ├── math.py
│   │   │   ├── matlab.py
│   │   │   ├── maxima.py
│   │   │   ├── meson.py
│   │   │   ├── mime.py
│   │   │   ├── minecraft.py
│   │   │   ├── mips.py
│   │   │   ├── ml.py
│   │   │   ├── modeling.py
│   │   │   ├── modula2.py
│   │   │   ├── mojo.py
│   │   │   ├── monte.py
│   │   │   ├── mosel.py
│   │   │   ├── ncl.py
│   │   │   ├── nimrod.py
│   │   │   ├── nit.py
│   │   │   ├── nix.py
│   │   │   ├── numbair.py
│   │   │   ├── oberon.py
│   │   │   ├── objective.py
│   │   │   ├── ooc.py
│   │   │   ├── openscad.py
│   │   │   ├── other.py
│   │   │   ├── parasail.py
│   │   │   ├── parsers.py
│   │   │   ├── pascal.py
│   │   │   ├── pawn.py
│   │   │   ├── pddl.py
│   │   │   ├── perl.py
│   │   │   ├── phix.py
│   │   │   ├── php.py
│   │   │   ├── pointless.py
│   │   │   ├── pony.py
│   │   │   ├── praat.py
│   │   │   ├── procfile.py
│   │   │   ├── prolog.py
│   │   │   ├── promql.py
│   │   │   ├── prql.py
│   │   │   ├── ptx.py
│   │   │   ├── python.py
│   │   │   ├── q.py
│   │   │   ├── qlik.py
│   │   │   ├── qvt.py
│   │   │   ├── r.py
│   │   │   ├── rdf.py
│   │   │   ├── rebol.py
│   │   │   ├── rego.py
│   │   │   ├── resource.py
│   │   │   ├── ride.py
│   │   │   ├── rita.py
│   │   │   ├── rnc.py
│   │   │   ├── roboconf.py
│   │   │   ├── robotframework.py
│   │   │   ├── ruby.py
│   │   │   ├── rust.py
│   │   │   ├── sas.py
│   │   │   ├── savi.py
│   │   │   ├── scdoc.py
│   │   │   ├── scripting.py
│   │   │   ├── sgf.py
│   │   │   ├── shell.py
│   │   │   ├── sieve.py
│   │   │   ├── slash.py
│   │   │   ├── smalltalk.py
│   │   │   ├── smithy.py
│   │   │   ├── smv.py
│   │   │   ├── snobol.py
│   │   │   ├── solidity.py
│   │   │   ├── soong.py
│   │   │   ├── sophia.py
│   │   │   ├── special.py
│   │   │   ├── spice.py
│   │   │   ├── sql.py
│   │   │   ├── srcinfo.py
│   │   │   ├── stata.py
│   │   │   ├── supercollider.py
│   │   │   ├── tablegen.py
│   │   │   ├── tact.py
│   │   │   ├── tal.py
│   │   │   ├── tcl.py
│   │   │   ├── teal.py
│   │   │   ├── templates.py
│   │   │   ├── teraterm.py
│   │   │   ├── testing.py
│   │   │   ├── text.py
│   │   │   ├── textedit.py
│   │   │   ├── textfmts.py
│   │   │   ├── theorem.py
│   │   │   ├── thingsdb.py
│   │   │   ├── tlb.py
│   │   │   ├── tls.py
│   │   │   ├── tnt.py
│   │   │   ├── trafficscript.py
│   │   │   ├── typoscript.py
│   │   │   ├── typst.py
│   │   │   ├── ul4.py
│   │   │   ├── unicon.py
│   │   │   ├── urbi.py
│   │   │   ├── usd.py
│   │   │   ├── varnish.py
│   │   │   ├── verification.py
│   │   │   ├── verifpal.py
│   │   │   ├── vip.py
│   │   │   ├── vyper.py
│   │   │   ├── web.py
│   │   │   ├── webassembly.py
│   │   │   ├── webidl.py
│   │   │   ├── webmisc.py
│   │   │   ├── wgsl.py
│   │   │   ├── whiley.py
│   │   │   ├── wowtoc.py
│   │   │   ├── wren.py
│   │   │   ├── x10.py
│   │   │   ├── xorg.py
│   │   │   ├── yang.py
│   │   │   ├── yara.py
│   │   │   └── zig.py
│   │   ├── modeline.py
│   │   ├── plugin.py
│   │   ├── regexopt.py
│   │   ├── scanner.py
│   │   ├── sphinxext.py
│   │   ├── style.py
│   │   ├── [01;34mstyles[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── _mapping.cpython-312.pyc
│   │   │   │   ├── abap.cpython-312.pyc
│   │   │   │   ├── algol.cpython-312.pyc
│   │   │   │   ├── algol_nu.cpython-312.pyc
│   │   │   │   ├── arduino.cpython-312.pyc
│   │   │   │   ├── autumn.cpython-312.pyc
│   │   │   │   ├── borland.cpython-312.pyc
│   │   │   │   ├── bw.cpython-312.pyc
│   │   │   │   ├── coffee.cpython-312.pyc
│   │   │   │   ├── colorful.cpython-312.pyc
│   │   │   │   ├── default.cpython-312.pyc
│   │   │   │   ├── dracula.cpython-312.pyc
│   │   │   │   ├── emacs.cpython-312.pyc
│   │   │   │   ├── friendly.cpython-312.pyc
│   │   │   │   ├── friendly_grayscale.cpython-312.pyc
│   │   │   │   ├── fruity.cpython-312.pyc
│   │   │   │   ├── gh_dark.cpython-312.pyc
│   │   │   │   ├── gruvbox.cpython-312.pyc
│   │   │   │   ├── igor.cpython-312.pyc
│   │   │   │   ├── inkpot.cpython-312.pyc
│   │   │   │   ├── lightbulb.cpython-312.pyc
│   │   │   │   ├── lilypond.cpython-312.pyc
│   │   │   │   ├── lovelace.cpython-312.pyc
│   │   │   │   ├── manni.cpython-312.pyc
│   │   │   │   ├── material.cpython-312.pyc
│   │   │   │   ├── monokai.cpython-312.pyc
│   │   │   │   ├── murphy.cpython-312.pyc
│   │   │   │   ├── native.cpython-312.pyc
│   │   │   │   ├── nord.cpython-312.pyc
│   │   │   │   ├── onedark.cpython-312.pyc
│   │   │   │   ├── paraiso_dark.cpython-312.pyc
│   │   │   │   ├── paraiso_light.cpython-312.pyc
│   │   │   │   ├── pastie.cpython-312.pyc
│   │   │   │   ├── perldoc.cpython-312.pyc
│   │   │   │   ├── rainbow_dash.cpython-312.pyc
│   │   │   │   ├── rrt.cpython-312.pyc
│   │   │   │   ├── sas.cpython-312.pyc
│   │   │   │   ├── solarized.cpython-312.pyc
│   │   │   │   ├── staroffice.cpython-312.pyc
│   │   │   │   ├── stata_dark.cpython-312.pyc
│   │   │   │   ├── stata_light.cpython-312.pyc
│   │   │   │   ├── tango.cpython-312.pyc
│   │   │   │   ├── trac.cpython-312.pyc
│   │   │   │   ├── vim.cpython-312.pyc
│   │   │   │   ├── vs.cpython-312.pyc
│   │   │   │   ├── xcode.cpython-312.pyc
│   │   │   │   └── zenburn.cpython-312.pyc
│   │   │   ├── _mapping.py
│   │   │   ├── abap.py
│   │   │   ├── algol.py
│   │   │   ├── algol_nu.py
│   │   │   ├── arduino.py
│   │   │   ├── autumn.py
│   │   │   ├── borland.py
│   │   │   ├── bw.py
│   │   │   ├── coffee.py
│   │   │   ├── colorful.py
│   │   │   ├── default.py
│   │   │   ├── dracula.py
│   │   │   ├── emacs.py
│   │   │   ├── friendly.py
│   │   │   ├── friendly_grayscale.py
│   │   │   ├── fruity.py
│   │   │   ├── gh_dark.py
│   │   │   ├── gruvbox.py
│   │   │   ├── igor.py
│   │   │   ├── inkpot.py
│   │   │   ├── lightbulb.py
│   │   │   ├── lilypond.py
│   │   │   ├── lovelace.py
│   │   │   ├── manni.py
│   │   │   ├── material.py
│   │   │   ├── monokai.py
│   │   │   ├── murphy.py
│   │   │   ├── native.py
│   │   │   ├── nord.py
│   │   │   ├── onedark.py
│   │   │   ├── paraiso_dark.py
│   │   │   ├── paraiso_light.py
│   │   │   ├── pastie.py
│   │   │   ├── perldoc.py
│   │   │   ├── rainbow_dash.py
│   │   │   ├── rrt.py
│   │   │   ├── sas.py
│   │   │   ├── solarized.py
│   │   │   ├── staroffice.py
│   │   │   ├── stata_dark.py
│   │   │   ├── stata_light.py
│   │   │   ├── tango.py
│   │   │   ├── trac.py
│   │   │   ├── vim.py
│   │   │   ├── vs.py
│   │   │   ├── xcode.py
│   │   │   └── zenburn.py
│   │   ├── token.py
│   │   ├── unistring.py
│   │   └── util.py
│   ├── [01;34mpygments-2.19.2.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   ├── entry_points.txt
│   │   └── [01;34mlicenses[0m
│   │       ├── AUTHORS
│   │       └── LICENSE
│   ├── [01;34mpytest[0m
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── __main__.cpython-312.pyc
│   │   └── py.typed
│   ├── [01;34mpytest-9.0.2.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── REQUESTED
│   │   ├── WHEEL
│   │   ├── entry_points.txt
│   │   ├── [01;34mlicenses[0m
│   │   │   └── LICENSE
│   │   └── top_level.txt
│   ├── [01;34mpython_dotenv-1.2.2.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── REQUESTED
│   │   ├── WHEEL
│   │   ├── entry_points.txt
│   │   ├── [01;34mlicenses[0m
│   │   │   └── LICENSE
│   │   └── top_level.txt
│   ├── [01;34mpython_multipart[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── decoders.cpython-312.pyc
│   │   │   ├── exceptions.cpython-312.pyc
│   │   │   └── multipart.cpython-312.pyc
│   │   ├── decoders.py
│   │   ├── exceptions.py
│   │   ├── multipart.py
│   │   └── py.typed
│   ├── [01;34mpython_multipart-0.0.22.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── REQUESTED
│   │   ├── WHEEL
│   │   └── [01;34mlicenses[0m
│   │       └── LICENSE.txt
│   ├── [01;34mstarlette[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── _exception_handler.cpython-312.pyc
│   │   │   ├── _utils.cpython-312.pyc
│   │   │   ├── applications.cpython-312.pyc
│   │   │   ├── authentication.cpython-312.pyc
│   │   │   ├── background.cpython-312.pyc
│   │   │   ├── concurrency.cpython-312.pyc
│   │   │   ├── config.cpython-312.pyc
│   │   │   ├── convertors.cpython-312.pyc
│   │   │   ├── datastructures.cpython-312.pyc
│   │   │   ├── endpoints.cpython-312.pyc
│   │   │   ├── exceptions.cpython-312.pyc
│   │   │   ├── formparsers.cpython-312.pyc
│   │   │   ├── requests.cpython-312.pyc
│   │   │   ├── responses.cpython-312.pyc
│   │   │   ├── routing.cpython-312.pyc
│   │   │   ├── schemas.cpython-312.pyc
│   │   │   ├── staticfiles.cpython-312.pyc
│   │   │   ├── status.cpython-312.pyc
│   │   │   ├── templating.cpython-312.pyc
│   │   │   ├── testclient.cpython-312.pyc
│   │   │   ├── types.cpython-312.pyc
│   │   │   └── websockets.cpython-312.pyc
│   │   ├── _exception_handler.py
│   │   ├── _utils.py
│   │   ├── applications.py
│   │   ├── authentication.py
│   │   ├── background.py
│   │   ├── concurrency.py
│   │   ├── config.py
│   │   ├── convertors.py
│   │   ├── datastructures.py
│   │   ├── endpoints.py
│   │   ├── exceptions.py
│   │   ├── formparsers.py
│   │   ├── [01;34mmiddleware[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── authentication.cpython-312.pyc
│   │   │   │   ├── base.cpython-312.pyc
│   │   │   │   ├── cors.cpython-312.pyc
│   │   │   │   ├── errors.cpython-312.pyc
│   │   │   │   ├── exceptions.cpython-312.pyc
│   │   │   │   ├── gzip.cpython-312.pyc
│   │   │   │   ├── httpsredirect.cpython-312.pyc
│   │   │   │   ├── sessions.cpython-312.pyc
│   │   │   │   ├── trustedhost.cpython-312.pyc
│   │   │   │   └── wsgi.cpython-312.pyc
│   │   │   ├── authentication.py
│   │   │   ├── base.py
│   │   │   ├── cors.py
│   │   │   ├── errors.py
│   │   │   ├── exceptions.py
│   │   │   ├── gzip.py
│   │   │   ├── httpsredirect.py
│   │   │   ├── sessions.py
│   │   │   ├── trustedhost.py
│   │   │   └── wsgi.py
│   │   ├── py.typed
│   │   ├── requests.py
│   │   ├── responses.py
│   │   ├── routing.py
│   │   ├── schemas.py
│   │   ├── staticfiles.py
│   │   ├── status.py
│   │   ├── templating.py
│   │   ├── testclient.py
│   │   ├── types.py
│   │   └── websockets.py
│   ├── [01;34mstarlette-0.52.1.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   └── [01;34mlicenses[0m
│   │       └── LICENSE.md
│   ├── [01;34mtyping_extensions-4.15.0.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   └── [01;34mlicenses[0m
│   │       └── LICENSE
│   ├── typing_extensions.py
│   ├── [01;34mtyping_inspection[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── introspection.cpython-312.pyc
│   │   │   └── typing_objects.cpython-312.pyc
│   │   ├── introspection.py
│   │   ├── py.typed
│   │   ├── typing_objects.py
│   │   └── typing_objects.pyi
│   ├── [01;34mtyping_inspection-0.4.2.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── WHEEL
│   │   └── [01;34mlicenses[0m
│   │       └── LICENSE
│   ├── [01;34muvicorn[0m
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── __main__.cpython-312.pyc
│   │   │   ├── _compat.cpython-312.pyc
│   │   │   ├── _subprocess.cpython-312.pyc
│   │   │   ├── _types.cpython-312.pyc
│   │   │   ├── config.cpython-312.pyc
│   │   │   ├── importer.cpython-312.pyc
│   │   │   ├── logging.cpython-312.pyc
│   │   │   ├── main.cpython-312.pyc
│   │   │   ├── server.cpython-312.pyc
│   │   │   └── workers.cpython-312.pyc
│   │   ├── _compat.py
│   │   ├── _subprocess.py
│   │   ├── _types.py
│   │   ├── config.py
│   │   ├── importer.py
│   │   ├── [01;34mlifespan[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── off.cpython-312.pyc
│   │   │   │   └── on.cpython-312.pyc
│   │   │   ├── off.py
│   │   │   └── on.py
│   │   ├── logging.py
│   │   ├── [01;34mloops[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── asyncio.cpython-312.pyc
│   │   │   │   ├── auto.cpython-312.pyc
│   │   │   │   └── uvloop.cpython-312.pyc
│   │   │   ├── asyncio.py
│   │   │   ├── auto.py
│   │   │   └── uvloop.py
│   │   ├── main.py
│   │   ├── [01;34mmiddleware[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── asgi2.cpython-312.pyc
│   │   │   │   ├── message_logger.cpython-312.pyc
│   │   │   │   ├── proxy_headers.cpython-312.pyc
│   │   │   │   └── wsgi.cpython-312.pyc
│   │   │   ├── asgi2.py
│   │   │   ├── message_logger.py
│   │   │   ├── proxy_headers.py
│   │   │   └── wsgi.py
│   │   ├── [01;34mprotocols[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   └── utils.cpython-312.pyc
│   │   │   ├── [01;34mhttp[0m
│   │   │   │   ├── __init__.py
│   │   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   │   ├── auto.cpython-312.pyc
│   │   │   │   │   ├── flow_control.cpython-312.pyc
│   │   │   │   │   ├── h11_impl.cpython-312.pyc
│   │   │   │   │   └── httptools_impl.cpython-312.pyc
│   │   │   │   ├── auto.py
│   │   │   │   ├── flow_control.py
│   │   │   │   ├── h11_impl.py
│   │   │   │   └── httptools_impl.py
│   │   │   ├── utils.py
│   │   │   └── [01;34mwebsockets[0m
│   │   │       ├── __init__.py
│   │   │       ├── [01;34m__pycache__[0m
│   │   │       │   ├── __init__.cpython-312.pyc
│   │   │       │   ├── auto.cpython-312.pyc
│   │   │       │   ├── websockets_impl.cpython-312.pyc
│   │   │       │   ├── websockets_sansio_impl.cpython-312.pyc
│   │   │       │   └── wsproto_impl.cpython-312.pyc
│   │   │       ├── auto.py
│   │   │       ├── websockets_impl.py
│   │   │       ├── websockets_sansio_impl.py
│   │   │       └── wsproto_impl.py
│   │   ├── py.typed
│   │   ├── server.py
│   │   ├── [01;34msupervisors[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── basereload.cpython-312.pyc
│   │   │   │   ├── multiprocess.cpython-312.pyc
│   │   │   │   ├── statreload.cpython-312.pyc
│   │   │   │   └── watchfilesreload.cpython-312.pyc
│   │   │   ├── basereload.py
│   │   │   ├── multiprocess.py
│   │   │   ├── statreload.py
│   │   │   └── watchfilesreload.py
│   │   └── workers.py
│   ├── [01;34muvicorn-0.41.0.dist-info[0m
│   │   ├── INSTALLER
│   │   ├── METADATA
│   │   ├── RECORD
│   │   ├── REQUESTED
│   │   ├── WHEEL
│   │   ├── entry_points.txt
│   │   └── [01;34mlicenses[0m
│   │       └── LICENSE.md
│   ├── [01;34mxmlschema[0m
│   │   ├── __init__.py
│   │   ├── [01;34m__pycache__[0m
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   ├── aliases.cpython-312.pyc
│   │   │   ├── cli.cpython-312.pyc
│   │   │   ├── dataobjects.cpython-312.pyc
│   │   │   ├── documents.cpython-312.pyc
│   │   │   ├── exceptions.cpython-312.pyc
│   │   │   ├── exports.cpython-312.pyc
│   │   │   ├── helpers.cpython-312.pyc
│   │   │   ├── limits.cpython-312.pyc
│   │   │   ├── locations.cpython-312.pyc
│   │   │   ├── names.cpython-312.pyc
│   │   │   ├── namespaces.cpython-312.pyc
│   │   │   ├── resources.cpython-312.pyc
│   │   │   ├── translation.cpython-312.pyc
│   │   │   └── xpath3.cpython-312.pyc
│   │   ├── aliases.py
│   │   ├── cli.py
│   │   ├── [01;34mconverters[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── abdera.cpython-312.pyc
│   │   │   │   ├── badgerfish.cpython-312.pyc
│   │   │   │   ├── columnar.cpython-312.pyc
│   │   │   │   ├── default.cpython-312.pyc
│   │   │   │   ├── gdata.cpython-312.pyc
│   │   │   │   ├── jsonml.cpython-312.pyc
│   │   │   │   ├── parker.cpython-312.pyc
│   │   │   │   └── unordered.cpython-312.pyc
│   │   │   ├── abdera.py
│   │   │   ├── badgerfish.py
│   │   │   ├── columnar.py
│   │   │   ├── default.py
│   │   │   ├── gdata.py
│   │   │   ├── jsonml.py
│   │   │   ├── parker.py
│   │   │   └── unordered.py
│   │   ├── dataobjects.py
│   │   ├── documents.py
│   │   ├── exceptions.py
│   │   ├── exports.py
│   │   ├── [01;34mextras[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── codegen.cpython-312.pyc
│   │   │   │   └── wsdl.cpython-312.pyc
│   │   │   ├── codegen.py
│   │   │   ├── [01;34mtemplates[0m
│   │   │   │   └── [01;34mpython[0m
│   │   │   │       ├── bindings.py.jinja
│   │   │   │       └── sample.py.jinja
│   │   │   └── wsdl.py
│   │   ├── helpers.py
│   │   ├── limits.py
│   │   ├── [01;34mlocale[0m
│   │   │   ├── [01;34men[0m
│   │   │   │   └── [01;34mLC_MESSAGES[0m
│   │   │   │       ├── xmlschema.mo
│   │   │   │       └── xmlschema.po
│   │   │   ├── [01;34mit[0m
│   │   │   │   └── [01;34mLC_MESSAGES[0m
│   │   │   │       ├── xmlschema.mo
│   │   │   │       └── xmlschema.po
│   │   │   ├── [01;34mpl[0m
│   │   │   │   └── [01;34mLC_MESSAGES[0m
│   │   │   │       ├── xmlschema.mo
│   │   │   │       └── xmlschema.po
│   │   │   └── [01;34mru[0m
│   │   │       └── [01;34mLC_MESSAGES[0m
│   │   │           ├── xmlschema.mo
│   │   │           └── xmlschema.po
│   │   ├── locations.py
│   │   ├── names.py
│   │   ├── namespaces.py
│   │   ├── py.typed
│   │   ├── resources.py
│   │   ├── [01;34mschemas[0m
│   │   │   ├── [01;34mDSIG[0m
│   │   │   │   ├── xmldsig-core-schema.xsd
│   │   │   │   └── xmldsig11-schema.xsd
│   │   │   ├── [01;34mHFP[0m
│   │   │   │   └── XMLSchema-hasFacetAndProperty_minimal.xsd
│   │   │   ├── [01;34mVC[0m
│   │   │   │   └── XMLSchema-versioning.xsd
│   │   │   ├── [01;34mWSDL[0m
│   │   │   │   ├── soap-encoding.xsd
│   │   │   │   ├── soap-envelope.xsd
│   │   │   │   ├── wsdl-soap.xsd
│   │   │   │   └── wsdl.xsd
│   │   │   ├── [01;34mXENC[0m
│   │   │   │   ├── xenc-schema-11.xsd
│   │   │   │   └── xenc-schema.xsd
│   │   │   ├── [01;34mXHTML[0m
│   │   │   │   └── xhtml1-strict.xsd
│   │   │   ├── [01;34mXLINK[0m
│   │   │   │   └── xlink.xsd
│   │   │   ├── [01;34mXML[0m
│   │   │   │   └── xml_minimal.xsd
│   │   │   ├── [01;34mXSD_1.0[0m
│   │   │   │   ├── XMLSchema.xsd
│   │   │   │   └── datatypes.xsd
│   │   │   ├── [01;34mXSD_1.1[0m
│   │   │   │   ├── XMLSchema.xsd
│   │   │   │   ├── datatypes.xsd
│   │   │   │   └── xsd11-extra.xsd
│   │   │   └── [01;34mXSI[0m
│   │   │       └── XMLSchema-instance_minimal.xsd
│   │   ├── [01;34mtesting[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── _builders.cpython-312.pyc
│   │   │   │   ├── _case_class.cpython-312.pyc
│   │   │   │   ├── _factory.cpython-312.pyc
│   │   │   │   ├── _helpers.cpython-312.pyc
│   │   │   │   └── _observers.cpython-312.pyc
│   │   │   ├── _builders.py
│   │   │   ├── _case_class.py
│   │   │   ├── _factory.py
│   │   │   ├── _helpers.py
│   │   │   └── _observers.py
│   │   ├── translation.py
│   │   ├── [01;34mvalidators[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── assertions.cpython-312.pyc
│   │   │   │   ├── attributes.cpython-312.pyc
│   │   │   │   ├── builtins.cpython-312.pyc
│   │   │   │   ├── complex_types.cpython-312.pyc
│   │   │   │   ├── elements.cpython-312.pyc
│   │   │   │   ├── exceptions.cpython-312.pyc
│   │   │   │   ├── facets.cpython-312.pyc
│   │   │   │   ├── global_maps.cpython-312.pyc
│   │   │   │   ├── groups.cpython-312.pyc
│   │   │   │   ├── helpers.cpython-312.pyc
│   │   │   │   ├── identities.cpython-312.pyc
│   │   │   │   ├── models.cpython-312.pyc
│   │   │   │   ├── notations.cpython-312.pyc
│   │   │   │   ├── particles.cpython-312.pyc
│   │   │   │   ├── schemas.cpython-312.pyc
│   │   │   │   ├── simple_types.cpython-312.pyc
│   │   │   │   ├── wildcards.cpython-312.pyc
│   │   │   │   └── xsdbase.cpython-312.pyc
│   │   │   ├── assertions.py
│   │   │   ├── attributes.py
│   │   │   ├── builtins.py
│   │   │   ├── complex_types.py
│   │   │   ├── elements.py
│   │   │   ├── exceptions.py
│   │   │   ├── facets.py
│   │   │   ├── global_maps.py
│   │   │   ├── groups.py
│   │   │   ├── helpers.py
│   │   │   ├── identities.py
│   │   │   ├── models.py
│   │   │   ├── notations.py
│   │   │   ├── particles.py
│   │   │   ├── schemas.py
│   │   │   ├── simple_types.py
│   │   │   ├── wildcards.py
│   │   │   └── xsdbase.py
│   │   ├── [01;34mxpath[0m
│   │   │   ├── __init__.py
│   │   │   ├── [01;34m__pycache__[0m
│   │   │   │   ├── __init__.cpython-312.pyc
│   │   │   │   ├── assertion_parser.cpython-312.pyc
│   │   │   │   ├── identity_parser.cpython-312.pyc
│   │   │   │   ├── mixin.cpython-312.pyc
│   │   │   │   └── proxy.cpython-312.pyc
│   │   │   ├── assertion_parser.py
│   │   │   ├── identity_parser.py
│   │   │   ├── mixin.py
│   │   │   └── proxy.py
│   │   └── xpath3.py
│   └── [01;34mxmlschema-3.4.2.dist-info[0m
│       ├── INSTALLER
│       ├── LICENSE
│       ├── METADATA
│       ├── RECORD
│       ├── REQUESTED
│       ├── WHEEL
│       ├── entry_points.txt
│       └── top_level.txt
├── requirements.txt
├── run.py
├── [01;34msrc[0m
│   └── [01;34mtests[0m
│       ├── test_api_endpoints.py
│       ├── test_schema_validation.py
│       └── test_xml_generation.py
├── [01;34mtests[0m
│   ├── __init__.py
│   ├── test_template.py
│   └── test_ubl.py
└── [01;34mvenv[0m
    ├── [01;34mbin[0m
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── [01;32mdotenv[0m
    │   ├── [01;32memail_validator[0m
    │   ├── [01;32mfastapi[0m
    │   ├── [01;32mpip[0m
    │   ├── [01;32mpip3[0m
    │   ├── [01;32mpip3.12[0m
    │   ├── [01;32mpy.test[0m
    │   ├── [01;32mpygmentize[0m
    │   ├── [01;32mpytest[0m
    │   ├── [01;36mpython[0m -> [01;32mpython3[0m
    │   ├── [01;36mpython3[0m -> [01;32m/usr/bin/python3[0m
    │   ├── [01;36mpython3.12[0m -> [01;32mpython3[0m
    │   ├── [01;32muvicorn[0m
    │   ├── [01;32mxmlschema-json2xml[0m
    │   ├── [01;32mxmlschema-validate[0m
    │   └── [01;32mxmlschema-xml2json[0m
    ├── [01;34minclude[0m
    │   └── [01;34mpython3.12[0m
    ├── [01;34mlib[0m
    │   └── [01;34mpython3.12[0m
    │       └── [01;34msite-packages[0m
    │           ├── [01;34m__pycache__[0m
    │           │   ├── py.cpython-312.pyc
    │           │   └── typing_extensions.cpython-312.pyc
    │           ├── [01;34m_pytest[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── _argcomplete.cpython-312.pyc
    │           │   │   ├── _version.cpython-312.pyc
    │           │   │   ├── cacheprovider.cpython-312.pyc
    │           │   │   ├── capture.cpython-312.pyc
    │           │   │   ├── compat.cpython-312.pyc
    │           │   │   ├── debugging.cpython-312.pyc
    │           │   │   ├── deprecated.cpython-312.pyc
    │           │   │   ├── doctest.cpython-312.pyc
    │           │   │   ├── faulthandler.cpython-312.pyc
    │           │   │   ├── fixtures.cpython-312.pyc
    │           │   │   ├── freeze_support.cpython-312.pyc
    │           │   │   ├── helpconfig.cpython-312.pyc
    │           │   │   ├── hookspec.cpython-312.pyc
    │           │   │   ├── junitxml.cpython-312.pyc
    │           │   │   ├── legacypath.cpython-312.pyc
    │           │   │   ├── logging.cpython-312.pyc
    │           │   │   ├── main.cpython-312.pyc
    │           │   │   ├── monkeypatch.cpython-312.pyc
    │           │   │   ├── nodes.cpython-312.pyc
    │           │   │   ├── outcomes.cpython-312.pyc
    │           │   │   ├── pastebin.cpython-312.pyc
    │           │   │   ├── pathlib.cpython-312.pyc
    │           │   │   ├── pytester.cpython-312.pyc
    │           │   │   ├── pytester_assertions.cpython-312.pyc
    │           │   │   ├── python.cpython-312.pyc
    │           │   │   ├── python_api.cpython-312.pyc
    │           │   │   ├── raises.cpython-312.pyc
    │           │   │   ├── recwarn.cpython-312.pyc
    │           │   │   ├── reports.cpython-312.pyc
    │           │   │   ├── runner.cpython-312.pyc
    │           │   │   ├── scope.cpython-312.pyc
    │           │   │   ├── setuponly.cpython-312.pyc
    │           │   │   ├── setupplan.cpython-312.pyc
    │           │   │   ├── skipping.cpython-312.pyc
    │           │   │   ├── stash.cpython-312.pyc
    │           │   │   ├── stepwise.cpython-312.pyc
    │           │   │   ├── subtests.cpython-312.pyc
    │           │   │   ├── terminal.cpython-312.pyc
    │           │   │   ├── terminalprogress.cpython-312.pyc
    │           │   │   ├── threadexception.cpython-312.pyc
    │           │   │   ├── timing.cpython-312.pyc
    │           │   │   ├── tmpdir.cpython-312.pyc
    │           │   │   ├── tracemalloc.cpython-312.pyc
    │           │   │   ├── unittest.cpython-312.pyc
    │           │   │   ├── unraisableexception.cpython-312.pyc
    │           │   │   ├── warning_types.cpython-312.pyc
    │           │   │   └── warnings.cpython-312.pyc
    │           │   ├── _argcomplete.py
    │           │   ├── [01;34m_code[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── code.cpython-312.pyc
    │           │   │   │   └── source.cpython-312.pyc
    │           │   │   ├── code.py
    │           │   │   └── source.py
    │           │   ├── [01;34m_io[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── pprint.cpython-312.pyc
    │           │   │   │   ├── saferepr.cpython-312.pyc
    │           │   │   │   ├── terminalwriter.cpython-312.pyc
    │           │   │   │   └── wcwidth.cpython-312.pyc
    │           │   │   ├── pprint.py
    │           │   │   ├── saferepr.py
    │           │   │   ├── terminalwriter.py
    │           │   │   └── wcwidth.py
    │           │   ├── [01;34m_py[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── error.cpython-312.pyc
    │           │   │   │   └── path.cpython-312.pyc
    │           │   │   ├── error.py
    │           │   │   └── path.py
    │           │   ├── _version.py
    │           │   ├── [01;34massertion[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── rewrite.cpython-312.pyc
    │           │   │   │   ├── truncate.cpython-312.pyc
    │           │   │   │   └── util.cpython-312.pyc
    │           │   │   ├── rewrite.py
    │           │   │   ├── truncate.py
    │           │   │   └── util.py
    │           │   ├── cacheprovider.py
    │           │   ├── capture.py
    │           │   ├── compat.py
    │           │   ├── [01;34mconfig[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── argparsing.cpython-312.pyc
    │           │   │   │   ├── compat.cpython-312.pyc
    │           │   │   │   ├── exceptions.cpython-312.pyc
    │           │   │   │   └── findpaths.cpython-312.pyc
    │           │   │   ├── argparsing.py
    │           │   │   ├── compat.py
    │           │   │   ├── exceptions.py
    │           │   │   └── findpaths.py
    │           │   ├── debugging.py
    │           │   ├── deprecated.py
    │           │   ├── doctest.py
    │           │   ├── faulthandler.py
    │           │   ├── fixtures.py
    │           │   ├── freeze_support.py
    │           │   ├── helpconfig.py
    │           │   ├── hookspec.py
    │           │   ├── junitxml.py
    │           │   ├── legacypath.py
    │           │   ├── logging.py
    │           │   ├── main.py
    │           │   ├── [01;34mmark[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── expression.cpython-312.pyc
    │           │   │   │   └── structures.cpython-312.pyc
    │           │   │   ├── expression.py
    │           │   │   └── structures.py
    │           │   ├── monkeypatch.py
    │           │   ├── nodes.py
    │           │   ├── outcomes.py
    │           │   ├── pastebin.py
    │           │   ├── pathlib.py
    │           │   ├── py.typed
    │           │   ├── pytester.py
    │           │   ├── pytester_assertions.py
    │           │   ├── python.py
    │           │   ├── python_api.py
    │           │   ├── raises.py
    │           │   ├── recwarn.py
    │           │   ├── reports.py
    │           │   ├── runner.py
    │           │   ├── scope.py
    │           │   ├── setuponly.py
    │           │   ├── setupplan.py
    │           │   ├── skipping.py
    │           │   ├── stash.py
    │           │   ├── stepwise.py
    │           │   ├── subtests.py
    │           │   ├── terminal.py
    │           │   ├── terminalprogress.py
    │           │   ├── threadexception.py
    │           │   ├── timing.py
    │           │   ├── tmpdir.py
    │           │   ├── tracemalloc.py
    │           │   ├── unittest.py
    │           │   ├── unraisableexception.py
    │           │   ├── warning_types.py
    │           │   └── warnings.py
    │           ├── [01;34mannotated_doc[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   └── main.cpython-312.pyc
    │           │   ├── main.py
    │           │   └── py.typed
    │           ├── [01;34mannotated_doc-0.0.4.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   └── [01;34mlicenses[0m
    │           │       └── LICENSE
    │           ├── [01;34mannotated_types[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   └── test_cases.cpython-312.pyc
    │           │   ├── py.typed
    │           │   └── test_cases.py
    │           ├── [01;34mannotated_types-0.7.0.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── [01;34mlicenses[0m
    │           │       └── LICENSE
    │           ├── [01;34manyio[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312-pytest-9.0.2.pyc
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── from_thread.cpython-312-pytest-9.0.2.pyc
    │           │   │   ├── from_thread.cpython-312.pyc
    │           │   │   ├── functools.cpython-312.pyc
    │           │   │   ├── lowlevel.cpython-312-pytest-9.0.2.pyc
    │           │   │   ├── lowlevel.cpython-312.pyc
    │           │   │   ├── pytest_plugin.cpython-312-pytest-9.0.2.pyc
    │           │   │   ├── pytest_plugin.cpython-312.pyc
    │           │   │   ├── to_interpreter.cpython-312.pyc
    │           │   │   ├── to_process.cpython-312.pyc
    │           │   │   ├── to_thread.cpython-312-pytest-9.0.2.pyc
    │           │   │   └── to_thread.cpython-312.pyc
    │           │   ├── [01;34m_backends[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── _asyncio.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _asyncio.cpython-312.pyc
    │           │   │   │   ├── _trio.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   └── _trio.cpython-312.pyc
    │           │   │   ├── _asyncio.py
    │           │   │   └── _trio.py
    │           │   ├── [01;34m_core[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── _asyncio_selector_thread.cpython-312.pyc
    │           │   │   │   ├── _contextmanagers.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _contextmanagers.cpython-312.pyc
    │           │   │   │   ├── _eventloop.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _eventloop.cpython-312.pyc
    │           │   │   │   ├── _exceptions.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _exceptions.cpython-312.pyc
    │           │   │   │   ├── _fileio.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _fileio.cpython-312.pyc
    │           │   │   │   ├── _resources.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _resources.cpython-312.pyc
    │           │   │   │   ├── _signals.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _signals.cpython-312.pyc
    │           │   │   │   ├── _sockets.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _sockets.cpython-312.pyc
    │           │   │   │   ├── _streams.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _streams.cpython-312.pyc
    │           │   │   │   ├── _subprocesses.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _subprocesses.cpython-312.pyc
    │           │   │   │   ├── _synchronization.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _synchronization.cpython-312.pyc
    │           │   │   │   ├── _tasks.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _tasks.cpython-312.pyc
    │           │   │   │   ├── _tempfile.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _tempfile.cpython-312.pyc
    │           │   │   │   ├── _testing.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _testing.cpython-312.pyc
    │           │   │   │   ├── _typedattr.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   └── _typedattr.cpython-312.pyc
    │           │   │   ├── _asyncio_selector_thread.py
    │           │   │   ├── _contextmanagers.py
    │           │   │   ├── _eventloop.py
    │           │   │   ├── _exceptions.py
    │           │   │   ├── _fileio.py
    │           │   │   ├── _resources.py
    │           │   │   ├── _signals.py
    │           │   │   ├── _sockets.py
    │           │   │   ├── _streams.py
    │           │   │   ├── _subprocesses.py
    │           │   │   ├── _synchronization.py
    │           │   │   ├── _tasks.py
    │           │   │   ├── _tempfile.py
    │           │   │   ├── _testing.py
    │           │   │   └── _typedattr.py
    │           │   ├── [01;34mabc[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── _eventloop.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _eventloop.cpython-312.pyc
    │           │   │   │   ├── _resources.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _resources.cpython-312.pyc
    │           │   │   │   ├── _sockets.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _sockets.cpython-312.pyc
    │           │   │   │   ├── _streams.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _streams.cpython-312.pyc
    │           │   │   │   ├── _subprocesses.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _subprocesses.cpython-312.pyc
    │           │   │   │   ├── _tasks.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── _tasks.cpython-312.pyc
    │           │   │   │   ├── _testing.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   └── _testing.cpython-312.pyc
    │           │   │   ├── _eventloop.py
    │           │   │   ├── _resources.py
    │           │   │   ├── _sockets.py
    │           │   │   ├── _streams.py
    │           │   │   ├── _subprocesses.py
    │           │   │   ├── _tasks.py
    │           │   │   └── _testing.py
    │           │   ├── from_thread.py
    │           │   ├── functools.py
    │           │   ├── lowlevel.py
    │           │   ├── py.typed
    │           │   ├── pytest_plugin.py
    │           │   ├── [01;34mstreams[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── buffered.cpython-312.pyc
    │           │   │   │   ├── file.cpython-312.pyc
    │           │   │   │   ├── memory.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── memory.cpython-312.pyc
    │           │   │   │   ├── stapled.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   ├── stapled.cpython-312.pyc
    │           │   │   │   ├── text.cpython-312.pyc
    │           │   │   │   ├── tls.cpython-312-pytest-9.0.2.pyc
    │           │   │   │   └── tls.cpython-312.pyc
    │           │   │   ├── buffered.py
    │           │   │   ├── file.py
    │           │   │   ├── memory.py
    │           │   │   ├── stapled.py
    │           │   │   ├── text.py
    │           │   │   └── tls.py
    │           │   ├── to_interpreter.py
    │           │   ├── to_process.py
    │           │   └── to_thread.py
    │           ├── [01;34manyio-4.12.1.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   ├── [01;34mlicenses[0m
    │           │   │   └── LICENSE
    │           │   └── top_level.txt
    │           ├── [01;34mclick[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── _compat.cpython-312.pyc
    │           │   │   ├── _termui_impl.cpython-312.pyc
    │           │   │   ├── _textwrap.cpython-312.pyc
    │           │   │   ├── _utils.cpython-312.pyc
    │           │   │   ├── _winconsole.cpython-312.pyc
    │           │   │   ├── core.cpython-312.pyc
    │           │   │   ├── decorators.cpython-312.pyc
    │           │   │   ├── exceptions.cpython-312.pyc
    │           │   │   ├── formatting.cpython-312.pyc
    │           │   │   ├── globals.cpython-312.pyc
    │           │   │   ├── parser.cpython-312.pyc
    │           │   │   ├── shell_completion.cpython-312.pyc
    │           │   │   ├── termui.cpython-312.pyc
    │           │   │   ├── testing.cpython-312.pyc
    │           │   │   ├── types.cpython-312.pyc
    │           │   │   └── utils.cpython-312.pyc
    │           │   ├── _compat.py
    │           │   ├── _termui_impl.py
    │           │   ├── _textwrap.py
    │           │   ├── _utils.py
    │           │   ├── _winconsole.py
    │           │   ├── core.py
    │           │   ├── decorators.py
    │           │   ├── exceptions.py
    │           │   ├── formatting.py
    │           │   ├── globals.py
    │           │   ├── parser.py
    │           │   ├── py.typed
    │           │   ├── shell_completion.py
    │           │   ├── termui.py
    │           │   ├── testing.py
    │           │   ├── types.py
    │           │   └── utils.py
    │           ├── [01;34mclick-8.3.1.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── [01;34mlicenses[0m
    │           │       └── LICENSE.txt
    │           ├── [01;34mdns[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── _asyncbackend.cpython-312.pyc
    │           │   │   ├── _asyncio_backend.cpython-312.pyc
    │           │   │   ├── _ddr.cpython-312.pyc
    │           │   │   ├── _features.cpython-312.pyc
    │           │   │   ├── _immutable_ctx.cpython-312.pyc
    │           │   │   ├── _no_ssl.cpython-312.pyc
    │           │   │   ├── _tls_util.cpython-312.pyc
    │           │   │   ├── _trio_backend.cpython-312.pyc
    │           │   │   ├── asyncbackend.cpython-312.pyc
    │           │   │   ├── asyncquery.cpython-312.pyc
    │           │   │   ├── asyncresolver.cpython-312.pyc
    │           │   │   ├── btree.cpython-312.pyc
    │           │   │   ├── btreezone.cpython-312.pyc
    │           │   │   ├── dnssec.cpython-312.pyc
    │           │   │   ├── dnssectypes.cpython-312.pyc
    │           │   │   ├── e164.cpython-312.pyc
    │           │   │   ├── edns.cpython-312.pyc
    │           │   │   ├── entropy.cpython-312.pyc
    │           │   │   ├── enum.cpython-312.pyc
    │           │   │   ├── exception.cpython-312.pyc
    │           │   │   ├── flags.cpython-312.pyc
    │           │   │   ├── grange.cpython-312.pyc
    │           │   │   ├── immutable.cpython-312.pyc
    │           │   │   ├── inet.cpython-312.pyc
    │           │   │   ├── ipv4.cpython-312.pyc
    │           │   │   ├── ipv6.cpython-312.pyc
    │           │   │   ├── message.cpython-312.pyc
    │           │   │   ├── name.cpython-312.pyc
    │           │   │   ├── namedict.cpython-312.pyc
    │           │   │   ├── nameserver.cpython-312.pyc
    │           │   │   ├── node.cpython-312.pyc
    │           │   │   ├── opcode.cpython-312.pyc
    │           │   │   ├── query.cpython-312.pyc
    │           │   │   ├── rcode.cpython-312.pyc
    │           │   │   ├── rdata.cpython-312.pyc
    │           │   │   ├── rdataclass.cpython-312.pyc
    │           │   │   ├── rdataset.cpython-312.pyc
    │           │   │   ├── rdatatype.cpython-312.pyc
    │           │   │   ├── renderer.cpython-312.pyc
    │           │   │   ├── resolver.cpython-312.pyc
    │           │   │   ├── reversename.cpython-312.pyc
    │           │   │   ├── rrset.cpython-312.pyc
    │           │   │   ├── serial.cpython-312.pyc
    │           │   │   ├── set.cpython-312.pyc
    │           │   │   ├── tokenizer.cpython-312.pyc
    │           │   │   ├── transaction.cpython-312.pyc
    │           │   │   ├── tsig.cpython-312.pyc
    │           │   │   ├── tsigkeyring.cpython-312.pyc
    │           │   │   ├── ttl.cpython-312.pyc
    │           │   │   ├── update.cpython-312.pyc
    │           │   │   ├── version.cpython-312.pyc
    │           │   │   ├── versioned.cpython-312.pyc
    │           │   │   ├── win32util.cpython-312.pyc
    │           │   │   ├── wire.cpython-312.pyc
    │           │   │   ├── xfr.cpython-312.pyc
    │           │   │   ├── zone.cpython-312.pyc
    │           │   │   ├── zonefile.cpython-312.pyc
    │           │   │   └── zonetypes.cpython-312.pyc
    │           │   ├── _asyncbackend.py
    │           │   ├── _asyncio_backend.py
    │           │   ├── _ddr.py
    │           │   ├── _features.py
    │           │   ├── _immutable_ctx.py
    │           │   ├── _no_ssl.py
    │           │   ├── _tls_util.py
    │           │   ├── _trio_backend.py
    │           │   ├── asyncbackend.py
    │           │   ├── asyncquery.py
    │           │   ├── asyncresolver.py
    │           │   ├── btree.py
    │           │   ├── btreezone.py
    │           │   ├── dnssec.py
    │           │   ├── [01;34mdnssecalgs[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── base.cpython-312.pyc
    │           │   │   │   ├── cryptography.cpython-312.pyc
    │           │   │   │   ├── dsa.cpython-312.pyc
    │           │   │   │   ├── ecdsa.cpython-312.pyc
    │           │   │   │   ├── eddsa.cpython-312.pyc
    │           │   │   │   └── rsa.cpython-312.pyc
    │           │   │   ├── base.py
    │           │   │   ├── cryptography.py
    │           │   │   ├── dsa.py
    │           │   │   ├── ecdsa.py
    │           │   │   ├── eddsa.py
    │           │   │   └── rsa.py
    │           │   ├── dnssectypes.py
    │           │   ├── e164.py
    │           │   ├── edns.py
    │           │   ├── entropy.py
    │           │   ├── enum.py
    │           │   ├── exception.py
    │           │   ├── flags.py
    │           │   ├── grange.py
    │           │   ├── immutable.py
    │           │   ├── inet.py
    │           │   ├── ipv4.py
    │           │   ├── ipv6.py
    │           │   ├── message.py
    │           │   ├── name.py
    │           │   ├── namedict.py
    │           │   ├── nameserver.py
    │           │   ├── node.py
    │           │   ├── opcode.py
    │           │   ├── py.typed
    │           │   ├── query.py
    │           │   ├── [01;34mquic[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── _asyncio.cpython-312.pyc
    │           │   │   │   ├── _common.cpython-312.pyc
    │           │   │   │   ├── _sync.cpython-312.pyc
    │           │   │   │   └── _trio.cpython-312.pyc
    │           │   │   ├── _asyncio.py
    │           │   │   ├── _common.py
    │           │   │   ├── _sync.py
    │           │   │   └── _trio.py
    │           │   ├── rcode.py
    │           │   ├── rdata.py
    │           │   ├── rdataclass.py
    │           │   ├── rdataset.py
    │           │   ├── rdatatype.py
    │           │   ├── [01;34mrdtypes[0m
    │           │   │   ├── [01;34mANY[0m
    │           │   │   │   ├── AFSDB.py
    │           │   │   │   ├── AMTRELAY.py
    │           │   │   │   ├── AVC.py
    │           │   │   │   ├── CAA.py
    │           │   │   │   ├── CDNSKEY.py
    │           │   │   │   ├── CDS.py
    │           │   │   │   ├── CERT.py
    │           │   │   │   ├── CNAME.py
    │           │   │   │   ├── CSYNC.py
    │           │   │   │   ├── DLV.py
    │           │   │   │   ├── DNAME.py
    │           │   │   │   ├── DNSKEY.py
    │           │   │   │   ├── DS.py
    │           │   │   │   ├── DSYNC.py
    │           │   │   │   ├── EUI48.py
    │           │   │   │   ├── EUI64.py
    │           │   │   │   ├── GPOS.py
    │           │   │   │   ├── HINFO.py
    │           │   │   │   ├── HIP.py
    │           │   │   │   ├── ISDN.py
    │           │   │   │   ├── L32.py
    │           │   │   │   ├── L64.py
    │           │   │   │   ├── LOC.py
    │           │   │   │   ├── LP.py
    │           │   │   │   ├── MX.py
    │           │   │   │   ├── NID.py
    │           │   │   │   ├── NINFO.py
    │           │   │   │   ├── NS.py
    │           │   │   │   ├── NSEC.py
    │           │   │   │   ├── NSEC3.py
    │           │   │   │   ├── NSEC3PARAM.py
    │           │   │   │   ├── OPENPGPKEY.py
    │           │   │   │   ├── OPT.py
    │           │   │   │   ├── PTR.py
    │           │   │   │   ├── RESINFO.py
    │           │   │   │   ├── RP.py
    │           │   │   │   ├── RRSIG.py
    │           │   │   │   ├── RT.py
    │           │   │   │   ├── SMIMEA.py
    │           │   │   │   ├── SOA.py
    │           │   │   │   ├── SPF.py
    │           │   │   │   ├── SSHFP.py
    │           │   │   │   ├── TKEY.py
    │           │   │   │   ├── TLSA.py
    │           │   │   │   ├── TSIG.py
    │           │   │   │   ├── TXT.py
    │           │   │   │   ├── URI.py
    │           │   │   │   ├── WALLET.py
    │           │   │   │   ├── X25.py
    │           │   │   │   ├── ZONEMD.py
    │           │   │   │   ├── __init__.py
    │           │   │   │   └── [01;34m__pycache__[0m
    │           │   │   │       ├── AFSDB.cpython-312.pyc
    │           │   │   │       ├── AMTRELAY.cpython-312.pyc
    │           │   │   │       ├── AVC.cpython-312.pyc
    │           │   │   │       ├── CAA.cpython-312.pyc
    │           │   │   │       ├── CDNSKEY.cpython-312.pyc
    │           │   │   │       ├── CDS.cpython-312.pyc
    │           │   │   │       ├── CERT.cpython-312.pyc
    │           │   │   │       ├── CNAME.cpython-312.pyc
    │           │   │   │       ├── CSYNC.cpython-312.pyc
    │           │   │   │       ├── DLV.cpython-312.pyc
    │           │   │   │       ├── DNAME.cpython-312.pyc
    │           │   │   │       ├── DNSKEY.cpython-312.pyc
    │           │   │   │       ├── DS.cpython-312.pyc
    │           │   │   │       ├── DSYNC.cpython-312.pyc
    │           │   │   │       ├── EUI48.cpython-312.pyc
    │           │   │   │       ├── EUI64.cpython-312.pyc
    │           │   │   │       ├── GPOS.cpython-312.pyc
    │           │   │   │       ├── HINFO.cpython-312.pyc
    │           │   │   │       ├── HIP.cpython-312.pyc
    │           │   │   │       ├── ISDN.cpython-312.pyc
    │           │   │   │       ├── L32.cpython-312.pyc
    │           │   │   │       ├── L64.cpython-312.pyc
    │           │   │   │       ├── LOC.cpython-312.pyc
    │           │   │   │       ├── LP.cpython-312.pyc
    │           │   │   │       ├── MX.cpython-312.pyc
    │           │   │   │       ├── NID.cpython-312.pyc
    │           │   │   │       ├── NINFO.cpython-312.pyc
    │           │   │   │       ├── NS.cpython-312.pyc
    │           │   │   │       ├── NSEC.cpython-312.pyc
    │           │   │   │       ├── NSEC3.cpython-312.pyc
    │           │   │   │       ├── NSEC3PARAM.cpython-312.pyc
    │           │   │   │       ├── OPENPGPKEY.cpython-312.pyc
    │           │   │   │       ├── OPT.cpython-312.pyc
    │           │   │   │       ├── PTR.cpython-312.pyc
    │           │   │   │       ├── RESINFO.cpython-312.pyc
    │           │   │   │       ├── RP.cpython-312.pyc
    │           │   │   │       ├── RRSIG.cpython-312.pyc
    │           │   │   │       ├── RT.cpython-312.pyc
    │           │   │   │       ├── SMIMEA.cpython-312.pyc
    │           │   │   │       ├── SOA.cpython-312.pyc
    │           │   │   │       ├── SPF.cpython-312.pyc
    │           │   │   │       ├── SSHFP.cpython-312.pyc
    │           │   │   │       ├── TKEY.cpython-312.pyc
    │           │   │   │       ├── TLSA.cpython-312.pyc
    │           │   │   │       ├── TSIG.cpython-312.pyc
    │           │   │   │       ├── TXT.cpython-312.pyc
    │           │   │   │       ├── URI.cpython-312.pyc
    │           │   │   │       ├── WALLET.cpython-312.pyc
    │           │   │   │       ├── X25.cpython-312.pyc
    │           │   │   │       ├── ZONEMD.cpython-312.pyc
    │           │   │   │       └── __init__.cpython-312.pyc
    │           │   │   ├── [01;34mCH[0m
    │           │   │   │   ├── A.py
    │           │   │   │   ├── __init__.py
    │           │   │   │   └── [01;34m__pycache__[0m
    │           │   │   │       ├── A.cpython-312.pyc
    │           │   │   │       └── __init__.cpython-312.pyc
    │           │   │   ├── [01;34mIN[0m
    │           │   │   │   ├── A.py
    │           │   │   │   ├── AAAA.py
    │           │   │   │   ├── APL.py
    │           │   │   │   ├── DHCID.py
    │           │   │   │   ├── HTTPS.py
    │           │   │   │   ├── IPSECKEY.py
    │           │   │   │   ├── KX.py
    │           │   │   │   ├── NAPTR.py
    │           │   │   │   ├── NSAP.py
    │           │   │   │   ├── NSAP_PTR.py
    │           │   │   │   ├── PX.py
    │           │   │   │   ├── SRV.py
    │           │   │   │   ├── SVCB.py
    │           │   │   │   ├── WKS.py
    │           │   │   │   ├── __init__.py
    │           │   │   │   └── [01;34m__pycache__[0m
    │           │   │   │       ├── A.cpython-312.pyc
    │           │   │   │       ├── AAAA.cpython-312.pyc
    │           │   │   │       ├── APL.cpython-312.pyc
    │           │   │   │       ├── DHCID.cpython-312.pyc
    │           │   │   │       ├── HTTPS.cpython-312.pyc
    │           │   │   │       ├── IPSECKEY.cpython-312.pyc
    │           │   │   │       ├── KX.cpython-312.pyc
    │           │   │   │       ├── NAPTR.cpython-312.pyc
    │           │   │   │       ├── NSAP.cpython-312.pyc
    │           │   │   │       ├── NSAP_PTR.cpython-312.pyc
    │           │   │   │       ├── PX.cpython-312.pyc
    │           │   │   │       ├── SRV.cpython-312.pyc
    │           │   │   │       ├── SVCB.cpython-312.pyc
    │           │   │   │       ├── WKS.cpython-312.pyc
    │           │   │   │       └── __init__.cpython-312.pyc
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── dnskeybase.cpython-312.pyc
    │           │   │   │   ├── dsbase.cpython-312.pyc
    │           │   │   │   ├── euibase.cpython-312.pyc
    │           │   │   │   ├── mxbase.cpython-312.pyc
    │           │   │   │   ├── nsbase.cpython-312.pyc
    │           │   │   │   ├── svcbbase.cpython-312.pyc
    │           │   │   │   ├── tlsabase.cpython-312.pyc
    │           │   │   │   ├── txtbase.cpython-312.pyc
    │           │   │   │   └── util.cpython-312.pyc
    │           │   │   ├── dnskeybase.py
    │           │   │   ├── dsbase.py
    │           │   │   ├── euibase.py
    │           │   │   ├── mxbase.py
    │           │   │   ├── nsbase.py
    │           │   │   ├── svcbbase.py
    │           │   │   ├── tlsabase.py
    │           │   │   ├── txtbase.py
    │           │   │   └── util.py
    │           │   ├── renderer.py
    │           │   ├── resolver.py
    │           │   ├── reversename.py
    │           │   ├── rrset.py
    │           │   ├── serial.py
    │           │   ├── set.py
    │           │   ├── tokenizer.py
    │           │   ├── transaction.py
    │           │   ├── tsig.py
    │           │   ├── tsigkeyring.py
    │           │   ├── ttl.py
    │           │   ├── update.py
    │           │   ├── version.py
    │           │   ├── versioned.py
    │           │   ├── win32util.py
    │           │   ├── wire.py
    │           │   ├── xfr.py
    │           │   ├── zone.py
    │           │   ├── zonefile.py
    │           │   └── zonetypes.py
    │           ├── [01;34mdnspython-2.8.0.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── [01;34mlicenses[0m
    │           │       └── LICENSE
    │           ├── [01;34mdotenv[0m
    │           │   ├── __init__.py
    │           │   ├── __main__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── __main__.cpython-312.pyc
    │           │   │   ├── cli.cpython-312.pyc
    │           │   │   ├── ipython.cpython-312.pyc
    │           │   │   ├── main.cpython-312.pyc
    │           │   │   ├── parser.cpython-312.pyc
    │           │   │   ├── variables.cpython-312.pyc
    │           │   │   └── version.cpython-312.pyc
    │           │   ├── cli.py
    │           │   ├── ipython.py
    │           │   ├── main.py
    │           │   ├── parser.py
    │           │   ├── py.typed
    │           │   ├── variables.py
    │           │   └── version.py
    │           ├── [01;34melementpath[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── _typing.cpython-312.pyc
    │           │   │   ├── aliases.cpython-312.pyc
    │           │   │   ├── collations.cpython-312.pyc
    │           │   │   ├── compare.cpython-312.pyc
    │           │   │   ├── decoder.cpython-312.pyc
    │           │   │   ├── etree.cpython-312.pyc
    │           │   │   ├── exceptions.cpython-312.pyc
    │           │   │   ├── helpers.cpython-312.pyc
    │           │   │   ├── namespaces.cpython-312.pyc
    │           │   │   ├── protocols.cpython-312.pyc
    │           │   │   ├── schema_proxy.cpython-312.pyc
    │           │   │   ├── sequence_types.cpython-312.pyc
    │           │   │   ├── serialization.cpython-312.pyc
    │           │   │   ├── tdop.cpython-312.pyc
    │           │   │   ├── tree_builders.cpython-312.pyc
    │           │   │   ├── xpath3.cpython-312.pyc
    │           │   │   ├── xpath_context.cpython-312.pyc
    │           │   │   ├── xpath_nodes.cpython-312.pyc
    │           │   │   ├── xpath_selectors.cpython-312.pyc
    │           │   │   └── xpath_tokens.cpython-312.pyc
    │           │   ├── _typing.py
    │           │   ├── aliases.py
    │           │   ├── collations.py
    │           │   ├── compare.py
    │           │   ├── [01;34mdatatypes[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── atomic_types.cpython-312.pyc
    │           │   │   │   ├── binary.cpython-312.pyc
    │           │   │   │   ├── datetime.cpython-312.pyc
    │           │   │   │   ├── numeric.cpython-312.pyc
    │           │   │   │   ├── proxies.cpython-312.pyc
    │           │   │   │   ├── qname.cpython-312.pyc
    │           │   │   │   ├── string.cpython-312.pyc
    │           │   │   │   ├── untyped.cpython-312.pyc
    │           │   │   │   └── uri.cpython-312.pyc
    │           │   │   ├── atomic_types.py
    │           │   │   ├── binary.py
    │           │   │   ├── datetime.py
    │           │   │   ├── numeric.py
    │           │   │   ├── proxies.py
    │           │   │   ├── qname.py
    │           │   │   ├── string.py
    │           │   │   ├── untyped.py
    │           │   │   └── uri.py
    │           │   ├── decoder.py
    │           │   ├── etree.py
    │           │   ├── exceptions.py
    │           │   ├── helpers.py
    │           │   ├── namespaces.py
    │           │   ├── protocols.py
    │           │   ├── py.typed
    │           │   ├── [01;34mregex[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── character_classes.cpython-312.pyc
    │           │   │   │   ├── codepoints.cpython-312.pyc
    │           │   │   │   ├── patterns.cpython-312.pyc
    │           │   │   │   ├── unicode_blocks.cpython-312.pyc
    │           │   │   │   ├── unicode_categories.cpython-312.pyc
    │           │   │   │   └── unicode_subsets.cpython-312.pyc
    │           │   │   ├── character_classes.py
    │           │   │   ├── codepoints.py
    │           │   │   ├── patterns.py
    │           │   │   ├── unicode_blocks.py
    │           │   │   ├── unicode_categories.py
    │           │   │   └── unicode_subsets.py
    │           │   ├── schema_proxy.py
    │           │   ├── sequence_types.py
    │           │   ├── serialization.py
    │           │   ├── tdop.py
    │           │   ├── tree_builders.py
    │           │   ├── [01;34mvalidators[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   └── __init__.cpython-312.pyc
    │           │   │   ├── analyze-string.xsd
    │           │   │   └── schema-for-json.xsd
    │           │   ├── [01;34mxpath1[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── _xpath1_axes.cpython-312.pyc
    │           │   │   │   ├── _xpath1_functions.cpython-312.pyc
    │           │   │   │   ├── _xpath1_operators.cpython-312.pyc
    │           │   │   │   └── xpath1_parser.cpython-312.pyc
    │           │   │   ├── _xpath1_axes.py
    │           │   │   ├── _xpath1_functions.py
    │           │   │   ├── _xpath1_operators.py
    │           │   │   └── xpath1_parser.py
    │           │   ├── [01;34mxpath2[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── _xpath2_constructors.cpython-312.pyc
    │           │   │   │   ├── _xpath2_functions.cpython-312.pyc
    │           │   │   │   ├── _xpath2_operators.cpython-312.pyc
    │           │   │   │   └── xpath2_parser.cpython-312.pyc
    │           │   │   ├── _xpath2_constructors.py
    │           │   │   ├── _xpath2_functions.py
    │           │   │   ├── _xpath2_operators.py
    │           │   │   └── xpath2_parser.py
    │           │   ├── xpath3.py
    │           │   ├── [01;34mxpath30[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── _translation_maps.cpython-312.pyc
    │           │   │   │   ├── _xpath30_functions.cpython-312.pyc
    │           │   │   │   ├── _xpath30_operators.cpython-312.pyc
    │           │   │   │   ├── xpath30_helpers.cpython-312.pyc
    │           │   │   │   └── xpath30_parser.cpython-312.pyc
    │           │   │   ├── _translation_maps.py
    │           │   │   ├── _xpath30_functions.py
    │           │   │   ├── _xpath30_operators.py
    │           │   │   ├── xpath30_helpers.py
    │           │   │   └── xpath30_parser.py
    │           │   ├── [01;34mxpath31[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── _xpath31_functions.cpython-312.pyc
    │           │   │   │   ├── _xpath31_operators.cpython-312.pyc
    │           │   │   │   └── xpath31_parser.cpython-312.pyc
    │           │   │   ├── _xpath31_functions.py
    │           │   │   ├── _xpath31_operators.py
    │           │   │   └── xpath31_parser.py
    │           │   ├── xpath_context.py
    │           │   ├── xpath_nodes.py
    │           │   ├── xpath_selectors.py
    │           │   └── xpath_tokens.py
    │           ├── [01;34melementpath-4.8.0.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── LICENSE
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── top_level.txt
    │           ├── [01;34memail_validator[0m
    │           │   ├── __init__.py
    │           │   ├── __main__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── __main__.cpython-312.pyc
    │           │   │   ├── deliverability.cpython-312.pyc
    │           │   │   ├── exceptions.cpython-312.pyc
    │           │   │   ├── rfc_constants.cpython-312.pyc
    │           │   │   ├── syntax.cpython-312.pyc
    │           │   │   ├── types.cpython-312.pyc
    │           │   │   ├── validate_email.cpython-312.pyc
    │           │   │   └── version.cpython-312.pyc
    │           │   ├── deliverability.py
    │           │   ├── exceptions.py
    │           │   ├── py.typed
    │           │   ├── rfc_constants.py
    │           │   ├── syntax.py
    │           │   ├── types.py
    │           │   ├── validate_email.py
    │           │   └── version.py
    │           ├── [01;34memail_validator-2.3.0.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── REQUESTED
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   ├── [01;34mlicenses[0m
    │           │   │   └── LICENSE
    │           │   └── top_level.txt
    │           ├── [01;34mfastapi[0m
    │           │   ├── __init__.py
    │           │   ├── __main__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── __main__.cpython-312.pyc
    │           │   │   ├── applications.cpython-312.pyc
    │           │   │   ├── background.cpython-312.pyc
    │           │   │   ├── cli.cpython-312.pyc
    │           │   │   ├── concurrency.cpython-312.pyc
    │           │   │   ├── datastructures.cpython-312.pyc
    │           │   │   ├── encoders.cpython-312.pyc
    │           │   │   ├── exception_handlers.cpython-312.pyc
    │           │   │   ├── exceptions.cpython-312.pyc
    │           │   │   ├── logger.cpython-312.pyc
    │           │   │   ├── param_functions.cpython-312.pyc
    │           │   │   ├── params.cpython-312.pyc
    │           │   │   ├── requests.cpython-312.pyc
    │           │   │   ├── responses.cpython-312.pyc
    │           │   │   ├── routing.cpython-312.pyc
    │           │   │   ├── sse.cpython-312.pyc
    │           │   │   ├── staticfiles.cpython-312.pyc
    │           │   │   ├── templating.cpython-312.pyc
    │           │   │   ├── testclient.cpython-312.pyc
    │           │   │   ├── types.cpython-312.pyc
    │           │   │   ├── utils.cpython-312.pyc
    │           │   │   └── websockets.cpython-312.pyc
    │           │   ├── [01;34m_compat[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── shared.cpython-312.pyc
    │           │   │   │   └── v2.cpython-312.pyc
    │           │   │   ├── shared.py
    │           │   │   └── v2.py
    │           │   ├── applications.py
    │           │   ├── background.py
    │           │   ├── cli.py
    │           │   ├── concurrency.py
    │           │   ├── datastructures.py
    │           │   ├── [01;34mdependencies[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── models.cpython-312.pyc
    │           │   │   │   └── utils.cpython-312.pyc
    │           │   │   ├── models.py
    │           │   │   └── utils.py
    │           │   ├── encoders.py
    │           │   ├── exception_handlers.py
    │           │   ├── exceptions.py
    │           │   ├── logger.py
    │           │   ├── [01;34mmiddleware[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── asyncexitstack.cpython-312.pyc
    │           │   │   │   ├── cors.cpython-312.pyc
    │           │   │   │   ├── gzip.cpython-312.pyc
    │           │   │   │   ├── httpsredirect.cpython-312.pyc
    │           │   │   │   ├── trustedhost.cpython-312.pyc
    │           │   │   │   └── wsgi.cpython-312.pyc
    │           │   │   ├── asyncexitstack.py
    │           │   │   ├── cors.py
    │           │   │   ├── gzip.py
    │           │   │   ├── httpsredirect.py
    │           │   │   ├── trustedhost.py
    │           │   │   └── wsgi.py
    │           │   ├── [01;34mopenapi[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── constants.cpython-312.pyc
    │           │   │   │   ├── docs.cpython-312.pyc
    │           │   │   │   ├── models.cpython-312.pyc
    │           │   │   │   └── utils.cpython-312.pyc
    │           │   │   ├── constants.py
    │           │   │   ├── docs.py
    │           │   │   ├── models.py
    │           │   │   └── utils.py
    │           │   ├── param_functions.py
    │           │   ├── params.py
    │           │   ├── py.typed
    │           │   ├── requests.py
    │           │   ├── responses.py
    │           │   ├── routing.py
    │           │   ├── [01;34msecurity[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── api_key.cpython-312.pyc
    │           │   │   │   ├── base.cpython-312.pyc
    │           │   │   │   ├── http.cpython-312.pyc
    │           │   │   │   ├── oauth2.cpython-312.pyc
    │           │   │   │   ├── open_id_connect_url.cpython-312.pyc
    │           │   │   │   └── utils.cpython-312.pyc
    │           │   │   ├── api_key.py
    │           │   │   ├── base.py
    │           │   │   ├── http.py
    │           │   │   ├── oauth2.py
    │           │   │   ├── open_id_connect_url.py
    │           │   │   └── utils.py
    │           │   ├── sse.py
    │           │   ├── staticfiles.py
    │           │   ├── templating.py
    │           │   ├── testclient.py
    │           │   ├── types.py
    │           │   ├── utils.py
    │           │   └── websockets.py
    │           ├── [01;34mfastapi-0.135.1.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── REQUESTED
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   └── [01;34mlicenses[0m
    │           │       └── LICENSE
    │           ├── [01;34mh11[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── _abnf.cpython-312.pyc
    │           │   │   ├── _connection.cpython-312.pyc
    │           │   │   ├── _events.cpython-312.pyc
    │           │   │   ├── _headers.cpython-312.pyc
    │           │   │   ├── _readers.cpython-312.pyc
    │           │   │   ├── _receivebuffer.cpython-312.pyc
    │           │   │   ├── _state.cpython-312.pyc
    │           │   │   ├── _util.cpython-312.pyc
    │           │   │   ├── _version.cpython-312.pyc
    │           │   │   └── _writers.cpython-312.pyc
    │           │   ├── _abnf.py
    │           │   ├── _connection.py
    │           │   ├── _events.py
    │           │   ├── _headers.py
    │           │   ├── _readers.py
    │           │   ├── _receivebuffer.py
    │           │   ├── _state.py
    │           │   ├── _util.py
    │           │   ├── _version.py
    │           │   ├── _writers.py
    │           │   └── py.typed
    │           ├── [01;34mh11-0.16.0.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   ├── [01;34mlicenses[0m
    │           │   │   └── LICENSE.txt
    │           │   └── top_level.txt
    │           ├── [01;34midna[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── codec.cpython-312.pyc
    │           │   │   ├── compat.cpython-312.pyc
    │           │   │   ├── core.cpython-312.pyc
    │           │   │   ├── idnadata.cpython-312.pyc
    │           │   │   ├── intranges.cpython-312.pyc
    │           │   │   ├── package_data.cpython-312.pyc
    │           │   │   └── uts46data.cpython-312.pyc
    │           │   ├── codec.py
    │           │   ├── compat.py
    │           │   ├── core.py
    │           │   ├── idnadata.py
    │           │   ├── intranges.py
    │           │   ├── package_data.py
    │           │   ├── py.typed
    │           │   └── uts46data.py
    │           ├── [01;34midna-3.11.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── [01;34mlicenses[0m
    │           │       └── LICENSE.md
    │           ├── [01;34miniconfig[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── _parse.cpython-312.pyc
    │           │   │   ├── _version.cpython-312.pyc
    │           │   │   └── exceptions.cpython-312.pyc
    │           │   ├── _parse.py
    │           │   ├── _version.py
    │           │   ├── exceptions.py
    │           │   └── py.typed
    │           ├── [01;34miniconfig-2.3.0.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   ├── [01;34mlicenses[0m
    │           │   │   └── LICENSE
    │           │   └── top_level.txt
    │           ├── [01;34mjinja2[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── _identifier.cpython-312.pyc
    │           │   │   ├── async_utils.cpython-312.pyc
    │           │   │   ├── bccache.cpython-312.pyc
    │           │   │   ├── compiler.cpython-312.pyc
    │           │   │   ├── constants.cpython-312.pyc
    │           │   │   ├── debug.cpython-312.pyc
    │           │   │   ├── defaults.cpython-312.pyc
    │           │   │   ├── environment.cpython-312.pyc
    │           │   │   ├── exceptions.cpython-312.pyc
    │           │   │   ├── ext.cpython-312.pyc
    │           │   │   ├── filters.cpython-312.pyc
    │           │   │   ├── idtracking.cpython-312.pyc
    │           │   │   ├── lexer.cpython-312.pyc
    │           │   │   ├── loaders.cpython-312.pyc
    │           │   │   ├── meta.cpython-312.pyc
    │           │   │   ├── nativetypes.cpython-312.pyc
    │           │   │   ├── nodes.cpython-312.pyc
    │           │   │   ├── optimizer.cpython-312.pyc
    │           │   │   ├── parser.cpython-312.pyc
    │           │   │   ├── runtime.cpython-312.pyc
    │           │   │   ├── sandbox.cpython-312.pyc
    │           │   │   ├── tests.cpython-312.pyc
    │           │   │   ├── utils.cpython-312.pyc
    │           │   │   └── visitor.cpython-312.pyc
    │           │   ├── _identifier.py
    │           │   ├── async_utils.py
    │           │   ├── bccache.py
    │           │   ├── compiler.py
    │           │   ├── constants.py
    │           │   ├── debug.py
    │           │   ├── defaults.py
    │           │   ├── environment.py
    │           │   ├── exceptions.py
    │           │   ├── ext.py
    │           │   ├── filters.py
    │           │   ├── idtracking.py
    │           │   ├── lexer.py
    │           │   ├── loaders.py
    │           │   ├── meta.py
    │           │   ├── nativetypes.py
    │           │   ├── nodes.py
    │           │   ├── optimizer.py
    │           │   ├── parser.py
    │           │   ├── py.typed
    │           │   ├── runtime.py
    │           │   ├── sandbox.py
    │           │   ├── tests.py
    │           │   ├── utils.py
    │           │   └── visitor.py
    │           ├── [01;34mjinja2-3.1.6.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── REQUESTED
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   └── [01;34mlicenses[0m
    │           │       └── LICENSE.txt
    │           ├── [01;34mlxml[0m
    │           │   ├── ElementInclude.py
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── ElementInclude.cpython-312.pyc
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── _elementpath.cpython-312.pyc
    │           │   │   ├── builder.cpython-312.pyc
    │           │   │   ├── cssselect.cpython-312.pyc
    │           │   │   ├── doctestcompare.cpython-312.pyc
    │           │   │   ├── pyclasslookup.cpython-312.pyc
    │           │   │   ├── sax.cpython-312.pyc
    │           │   │   └── usedoctest.cpython-312.pyc
    │           │   ├── [01;32m_elementpath.cpython-312-x86_64-linux-gnu.so[0m
    │           │   ├── _elementpath.py
    │           │   ├── apihelpers.pxi
    │           │   ├── [01;32mbuilder.cpython-312-x86_64-linux-gnu.so[0m
    │           │   ├── builder.py
    │           │   ├── classlookup.pxi
    │           │   ├── cleanup.pxi
    │           │   ├── cssselect.py
    │           │   ├── debug.pxi
    │           │   ├── docloader.pxi
    │           │   ├── doctestcompare.py
    │           │   ├── dtd.pxi
    │           │   ├── [01;32metree.cpython-312-x86_64-linux-gnu.so[0m
    │           │   ├── etree.h
    │           │   ├── etree.pyx
    │           │   ├── etree_api.h
    │           │   ├── extensions.pxi
    │           │   ├── [01;34mhtml[0m
    │           │   │   ├── ElementSoup.py
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── ElementSoup.cpython-312.pyc
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── _diffcommand.cpython-312.pyc
    │           │   │   │   ├── _html5builder.cpython-312.pyc
    │           │   │   │   ├── _setmixin.cpython-312.pyc
    │           │   │   │   ├── builder.cpython-312.pyc
    │           │   │   │   ├── clean.cpython-312.pyc
    │           │   │   │   ├── defs.cpython-312.pyc
    │           │   │   │   ├── diff.cpython-312.pyc
    │           │   │   │   ├── formfill.cpython-312.pyc
    │           │   │   │   ├── html5parser.cpython-312.pyc
    │           │   │   │   ├── soupparser.cpython-312.pyc
    │           │   │   │   └── usedoctest.cpython-312.pyc
    │           │   │   ├── _diffcommand.py
    │           │   │   ├── _html5builder.py
    │           │   │   ├── _setmixin.py
    │           │   │   ├── builder.py
    │           │   │   ├── clean.py
    │           │   │   ├── defs.py
    │           │   │   ├── [01;32mdiff.cpython-312-x86_64-linux-gnu.so[0m
    │           │   │   ├── diff.py
    │           │   │   ├── formfill.py
    │           │   │   ├── html5parser.py
    │           │   │   ├── soupparser.py
    │           │   │   └── usedoctest.py
    │           │   ├── [01;34mincludes[0m
    │           │   │   ├── __init__.pxd
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   └── __init__.cpython-312.pyc
    │           │   │   ├── c14n.pxd
    │           │   │   ├── config.pxd
    │           │   │   ├── dtdvalid.pxd
    │           │   │   ├── etree_defs.h
    │           │   │   ├── etreepublic.pxd
    │           │   │   ├── [01;34mextlibs[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   └── __init__.cpython-312.pyc
    │           │   │   │   ├── libcharset.h
    │           │   │   │   ├── localcharset.h
    │           │   │   │   ├── zconf.h
    │           │   │   │   └── zlib.h
    │           │   │   ├── htmlparser.pxd
    │           │   │   ├── [01;34mlibexslt[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   └── __init__.cpython-312.pyc
    │           │   │   │   ├── exslt.h
    │           │   │   │   ├── exsltconfig.h
    │           │   │   │   └── exsltexports.h
    │           │   │   ├── [01;34mlibxml[0m
    │           │   │   │   ├── HTMLparser.h
    │           │   │   │   ├── HTMLtree.h
    │           │   │   │   ├── SAX.h
    │           │   │   │   ├── SAX2.h
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   └── __init__.cpython-312.pyc
    │           │   │   │   ├── c14n.h
    │           │   │   │   ├── catalog.h
    │           │   │   │   ├── chvalid.h
    │           │   │   │   ├── debugXML.h
    │           │   │   │   ├── dict.h
    │           │   │   │   ├── encoding.h
    │           │   │   │   ├── entities.h
    │           │   │   │   ├── globals.h
    │           │   │   │   ├── hash.h
    │           │   │   │   ├── list.h
    │           │   │   │   ├── nanoftp.h
    │           │   │   │   ├── nanohttp.h
    │           │   │   │   ├── parser.h
    │           │   │   │   ├── parserInternals.h
    │           │   │   │   ├── relaxng.h
    │           │   │   │   ├── schemasInternals.h
    │           │   │   │   ├── schematron.h
    │           │   │   │   ├── threads.h
    │           │   │   │   ├── tree.h
    │           │   │   │   ├── uri.h
    │           │   │   │   ├── valid.h
    │           │   │   │   ├── xinclude.h
    │           │   │   │   ├── xlink.h
    │           │   │   │   ├── xmlIO.h
    │           │   │   │   ├── xmlautomata.h
    │           │   │   │   ├── xmlerror.h
    │           │   │   │   ├── xmlexports.h
    │           │   │   │   ├── xmlmemory.h
    │           │   │   │   ├── xmlmodule.h
    │           │   │   │   ├── xmlreader.h
    │           │   │   │   ├── xmlregexp.h
    │           │   │   │   ├── xmlsave.h
    │           │   │   │   ├── xmlschemas.h
    │           │   │   │   ├── xmlschemastypes.h
    │           │   │   │   ├── xmlstring.h
    │           │   │   │   ├── xmlunicode.h
    │           │   │   │   ├── xmlversion.h
    │           │   │   │   ├── xmlwriter.h
    │           │   │   │   ├── xpath.h
    │           │   │   │   ├── xpathInternals.h
    │           │   │   │   └── xpointer.h
    │           │   │   ├── [01;34mlibxslt[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   └── __init__.cpython-312.pyc
    │           │   │   │   ├── attributes.h
    │           │   │   │   ├── documents.h
    │           │   │   │   ├── extensions.h
    │           │   │   │   ├── extra.h
    │           │   │   │   ├── functions.h
    │           │   │   │   ├── imports.h
    │           │   │   │   ├── keys.h
    │           │   │   │   ├── namespaces.h
    │           │   │   │   ├── numbersInternals.h
    │           │   │   │   ├── pattern.h
    │           │   │   │   ├── preproc.h
    │           │   │   │   ├── security.h
    │           │   │   │   ├── templates.h
    │           │   │   │   ├── transform.h
    │           │   │   │   ├── variables.h
    │           │   │   │   ├── xslt.h
    │           │   │   │   ├── xsltInternals.h
    │           │   │   │   ├── xsltconfig.h
    │           │   │   │   ├── xsltexports.h
    │           │   │   │   ├── xsltlocale.h
    │           │   │   │   └── xsltutils.h
    │           │   │   ├── lxml-version.h
    │           │   │   ├── relaxng.pxd
    │           │   │   ├── schematron.pxd
    │           │   │   ├── tree.pxd
    │           │   │   ├── uri.pxd
    │           │   │   ├── xinclude.pxd
    │           │   │   ├── xmlerror.pxd
    │           │   │   ├── xmlparser.pxd
    │           │   │   ├── xmlschema.pxd
    │           │   │   ├── xpath.pxd
    │           │   │   └── xslt.pxd
    │           │   ├── [01;34misoschematron[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   └── __init__.cpython-312.pyc
    │           │   │   └── [01;34mresources[0m
    │           │   │       ├── [01;34mrng[0m
    │           │   │       │   └── iso-schematron.rng
    │           │   │       └── [01;34mxsl[0m
    │           │   │           ├── RNG2Schtrn.xsl
    │           │   │           ├── XSD2Schtrn.xsl
    │           │   │           └── [01;34miso-schematron-xslt1[0m
    │           │   │               ├── iso_abstract_expand.xsl
    │           │   │               ├── iso_dsdl_include.xsl
    │           │   │               ├── iso_schematron_message.xsl
    │           │   │               ├── iso_schematron_skeleton_for_xslt1.xsl
    │           │   │               ├── iso_svrl_for_xslt1.xsl
    │           │   │               └── readme.txt
    │           │   ├── iterparse.pxi
    │           │   ├── lxml.etree.h
    │           │   ├── lxml.etree_api.h
    │           │   ├── nsclasses.pxi
    │           │   ├── [01;32mobjectify.cpython-312-x86_64-linux-gnu.so[0m
    │           │   ├── objectify.pyx
    │           │   ├── objectpath.pxi
    │           │   ├── parser.pxi
    │           │   ├── parsertarget.pxi
    │           │   ├── proxy.pxi
    │           │   ├── public-api.pxi
    │           │   ├── pyclasslookup.py
    │           │   ├── readonlytree.pxi
    │           │   ├── relaxng.pxi
    │           │   ├── [01;32msax.cpython-312-x86_64-linux-gnu.so[0m
    │           │   ├── sax.py
    │           │   ├── saxparser.pxi
    │           │   ├── schematron.pxi
    │           │   ├── serializer.pxi
    │           │   ├── usedoctest.py
    │           │   ├── xinclude.pxi
    │           │   ├── xmlerror.pxi
    │           │   ├── xmlid.pxi
    │           │   ├── xmlschema.pxi
    │           │   ├── xpath.pxi
    │           │   ├── xslt.pxi
    │           │   └── xsltext.pxi
    │           ├── [01;34mlxml-5.3.0.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── LICENSE.txt
    │           │   ├── LICENSES.txt
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── REQUESTED
    │           │   ├── WHEEL
    │           │   └── top_level.txt
    │           ├── [01;34mmangum[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── adapter.cpython-312.pyc
    │           │   │   ├── exceptions.cpython-312.pyc
    │           │   │   └── types.cpython-312.pyc
    │           │   ├── adapter.py
    │           │   ├── exceptions.py
    │           │   ├── [01;34mhandlers[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── alb.cpython-312.pyc
    │           │   │   │   ├── api_gateway.cpython-312.pyc
    │           │   │   │   ├── lambda_at_edge.cpython-312.pyc
    │           │   │   │   └── utils.cpython-312.pyc
    │           │   │   ├── alb.py
    │           │   │   ├── api_gateway.py
    │           │   │   ├── lambda_at_edge.py
    │           │   │   └── utils.py
    │           │   ├── [01;34mprotocols[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── http.cpython-312.pyc
    │           │   │   │   └── lifespan.cpython-312.pyc
    │           │   │   ├── http.py
    │           │   │   └── lifespan.py
    │           │   ├── py.typed
    │           │   └── types.py
    │           ├── [01;34mmangum-0.21.0.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── REQUESTED
    │           │   ├── WHEEL
    │           │   └── [01;34mlicenses[0m
    │           │       └── LICENSE
    │           ├── [01;34mmarkupsafe[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   └── _native.cpython-312.pyc
    │           │   ├── _native.py
    │           │   ├── _speedups.c
    │           │   ├── [01;32m_speedups.cpython-312-x86_64-linux-gnu.so[0m
    │           │   ├── _speedups.pyi
    │           │   └── py.typed
    │           ├── [01;34mmarkupsafe-3.0.3.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   ├── [01;34mlicenses[0m
    │           │   │   └── LICENSE.txt
    │           │   └── top_level.txt
    │           ├── [01;34mmultipart[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── decoders.cpython-312.pyc
    │           │   │   ├── exceptions.cpython-312.pyc
    │           │   │   └── multipart.cpython-312.pyc
    │           │   ├── decoders.py
    │           │   ├── exceptions.py
    │           │   └── multipart.py
    │           ├── [01;34mpackaging[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── _elffile.cpython-312.pyc
    │           │   │   ├── _manylinux.cpython-312.pyc
    │           │   │   ├── _musllinux.cpython-312.pyc
    │           │   │   ├── _parser.cpython-312.pyc
    │           │   │   ├── _structures.cpython-312.pyc
    │           │   │   ├── _tokenizer.cpython-312.pyc
    │           │   │   ├── markers.cpython-312.pyc
    │           │   │   ├── metadata.cpython-312.pyc
    │           │   │   ├── pylock.cpython-312.pyc
    │           │   │   ├── requirements.cpython-312.pyc
    │           │   │   ├── specifiers.cpython-312.pyc
    │           │   │   ├── tags.cpython-312.pyc
    │           │   │   ├── utils.cpython-312.pyc
    │           │   │   └── version.cpython-312.pyc
    │           │   ├── _elffile.py
    │           │   ├── _manylinux.py
    │           │   ├── _musllinux.py
    │           │   ├── _parser.py
    │           │   ├── _structures.py
    │           │   ├── _tokenizer.py
    │           │   ├── [01;34mlicenses[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   └── _spdx.cpython-312.pyc
    │           │   │   └── _spdx.py
    │           │   ├── markers.py
    │           │   ├── metadata.py
    │           │   ├── py.typed
    │           │   ├── pylock.py
    │           │   ├── requirements.py
    │           │   ├── specifiers.py
    │           │   ├── tags.py
    │           │   ├── utils.py
    │           │   └── version.py
    │           ├── [01;34mpackaging-26.0.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── [01;34mlicenses[0m
    │           │       ├── LICENSE
    │           │       ├── LICENSE.APACHE
    │           │       └── LICENSE.BSD
    │           ├── [01;34mpip[0m
    │           │   ├── __init__.py
    │           │   ├── __main__.py
    │           │   ├── __pip-runner__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── __main__.cpython-312.pyc
    │           │   │   └── __pip-runner__.cpython-312.pyc
    │           │   ├── [01;34m_internal[0m
    │           │   │   ├── [01;32m__init__.py[0m
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── build_env.cpython-312.pyc
    │           │   │   │   ├── cache.cpython-312.pyc
    │           │   │   │   ├── configuration.cpython-312.pyc
    │           │   │   │   ├── exceptions.cpython-312.pyc
    │           │   │   │   ├── main.cpython-312.pyc
    │           │   │   │   ├── pyproject.cpython-312.pyc
    │           │   │   │   ├── self_outdated_check.cpython-312.pyc
    │           │   │   │   └── wheel_builder.cpython-312.pyc
    │           │   │   ├── build_env.py
    │           │   │   ├── cache.py
    │           │   │   ├── [01;34mcli[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── autocompletion.cpython-312.pyc
    │           │   │   │   │   ├── base_command.cpython-312.pyc
    │           │   │   │   │   ├── cmdoptions.cpython-312.pyc
    │           │   │   │   │   ├── command_context.cpython-312.pyc
    │           │   │   │   │   ├── index_command.cpython-312.pyc
    │           │   │   │   │   ├── main.cpython-312.pyc
    │           │   │   │   │   ├── main_parser.cpython-312.pyc
    │           │   │   │   │   ├── parser.cpython-312.pyc
    │           │   │   │   │   ├── progress_bars.cpython-312.pyc
    │           │   │   │   │   ├── req_command.cpython-312.pyc
    │           │   │   │   │   ├── spinners.cpython-312.pyc
    │           │   │   │   │   └── status_codes.cpython-312.pyc
    │           │   │   │   ├── autocompletion.py
    │           │   │   │   ├── base_command.py
    │           │   │   │   ├── cmdoptions.py
    │           │   │   │   ├── command_context.py
    │           │   │   │   ├── index_command.py
    │           │   │   │   ├── main.py
    │           │   │   │   ├── main_parser.py
    │           │   │   │   ├── parser.py
    │           │   │   │   ├── progress_bars.py
    │           │   │   │   ├── req_command.py
    │           │   │   │   ├── spinners.py
    │           │   │   │   └── status_codes.py
    │           │   │   ├── [01;34mcommands[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── cache.cpython-312.pyc
    │           │   │   │   │   ├── check.cpython-312.pyc
    │           │   │   │   │   ├── completion.cpython-312.pyc
    │           │   │   │   │   ├── configuration.cpython-312.pyc
    │           │   │   │   │   ├── debug.cpython-312.pyc
    │           │   │   │   │   ├── download.cpython-312.pyc
    │           │   │   │   │   ├── freeze.cpython-312.pyc
    │           │   │   │   │   ├── hash.cpython-312.pyc
    │           │   │   │   │   ├── help.cpython-312.pyc
    │           │   │   │   │   ├── index.cpython-312.pyc
    │           │   │   │   │   ├── inspect.cpython-312.pyc
    │           │   │   │   │   ├── install.cpython-312.pyc
    │           │   │   │   │   ├── list.cpython-312.pyc
    │           │   │   │   │   ├── lock.cpython-312.pyc
    │           │   │   │   │   ├── search.cpython-312.pyc
    │           │   │   │   │   ├── show.cpython-312.pyc
    │           │   │   │   │   ├── uninstall.cpython-312.pyc
    │           │   │   │   │   └── wheel.cpython-312.pyc
    │           │   │   │   ├── cache.py
    │           │   │   │   ├── check.py
    │           │   │   │   ├── completion.py
    │           │   │   │   ├── configuration.py
    │           │   │   │   ├── debug.py
    │           │   │   │   ├── download.py
    │           │   │   │   ├── freeze.py
    │           │   │   │   ├── hash.py
    │           │   │   │   ├── help.py
    │           │   │   │   ├── index.py
    │           │   │   │   ├── inspect.py
    │           │   │   │   ├── install.py
    │           │   │   │   ├── list.py
    │           │   │   │   ├── lock.py
    │           │   │   │   ├── search.py
    │           │   │   │   ├── show.py
    │           │   │   │   ├── uninstall.py
    │           │   │   │   └── wheel.py
    │           │   │   ├── configuration.py
    │           │   │   ├── [01;34mdistributions[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── base.cpython-312.pyc
    │           │   │   │   │   ├── installed.cpython-312.pyc
    │           │   │   │   │   ├── sdist.cpython-312.pyc
    │           │   │   │   │   └── wheel.cpython-312.pyc
    │           │   │   │   ├── base.py
    │           │   │   │   ├── installed.py
    │           │   │   │   ├── sdist.py
    │           │   │   │   └── wheel.py
    │           │   │   ├── exceptions.py
    │           │   │   ├── [01;34mindex[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── collector.cpython-312.pyc
    │           │   │   │   │   ├── package_finder.cpython-312.pyc
    │           │   │   │   │   └── sources.cpython-312.pyc
    │           │   │   │   ├── collector.py
    │           │   │   │   ├── package_finder.py
    │           │   │   │   └── sources.py
    │           │   │   ├── [01;34mlocations[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── _distutils.cpython-312.pyc
    │           │   │   │   │   ├── _sysconfig.cpython-312.pyc
    │           │   │   │   │   └── base.cpython-312.pyc
    │           │   │   │   ├── _distutils.py
    │           │   │   │   ├── _sysconfig.py
    │           │   │   │   └── base.py
    │           │   │   ├── main.py
    │           │   │   ├── [01;34mmetadata[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── _json.cpython-312.pyc
    │           │   │   │   │   ├── base.cpython-312.pyc
    │           │   │   │   │   └── pkg_resources.cpython-312.pyc
    │           │   │   │   ├── _json.py
    │           │   │   │   ├── base.py
    │           │   │   │   ├── [01;34mimportlib[0m
    │           │   │   │   │   ├── __init__.py
    │           │   │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   │   ├── _compat.cpython-312.pyc
    │           │   │   │   │   │   ├── _dists.cpython-312.pyc
    │           │   │   │   │   │   └── _envs.cpython-312.pyc
    │           │   │   │   │   ├── _compat.py
    │           │   │   │   │   ├── _dists.py
    │           │   │   │   │   └── _envs.py
    │           │   │   │   └── pkg_resources.py
    │           │   │   ├── [01;34mmodels[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── candidate.cpython-312.pyc
    │           │   │   │   │   ├── direct_url.cpython-312.pyc
    │           │   │   │   │   ├── format_control.cpython-312.pyc
    │           │   │   │   │   ├── index.cpython-312.pyc
    │           │   │   │   │   ├── installation_report.cpython-312.pyc
    │           │   │   │   │   ├── link.cpython-312.pyc
    │           │   │   │   │   ├── release_control.cpython-312.pyc
    │           │   │   │   │   ├── scheme.cpython-312.pyc
    │           │   │   │   │   ├── search_scope.cpython-312.pyc
    │           │   │   │   │   ├── selection_prefs.cpython-312.pyc
    │           │   │   │   │   ├── target_python.cpython-312.pyc
    │           │   │   │   │   └── wheel.cpython-312.pyc
    │           │   │   │   ├── candidate.py
    │           │   │   │   ├── direct_url.py
    │           │   │   │   ├── format_control.py
    │           │   │   │   ├── index.py
    │           │   │   │   ├── installation_report.py
    │           │   │   │   ├── link.py
    │           │   │   │   ├── release_control.py
    │           │   │   │   ├── scheme.py
    │           │   │   │   ├── search_scope.py
    │           │   │   │   ├── selection_prefs.py
    │           │   │   │   ├── target_python.py
    │           │   │   │   └── wheel.py
    │           │   │   ├── [01;34mnetwork[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── auth.cpython-312.pyc
    │           │   │   │   │   ├── cache.cpython-312.pyc
    │           │   │   │   │   ├── download.cpython-312.pyc
    │           │   │   │   │   ├── lazy_wheel.cpython-312.pyc
    │           │   │   │   │   ├── session.cpython-312.pyc
    │           │   │   │   │   ├── utils.cpython-312.pyc
    │           │   │   │   │   └── xmlrpc.cpython-312.pyc
    │           │   │   │   ├── auth.py
    │           │   │   │   ├── cache.py
    │           │   │   │   ├── download.py
    │           │   │   │   ├── lazy_wheel.py
    │           │   │   │   ├── session.py
    │           │   │   │   ├── utils.py
    │           │   │   │   └── xmlrpc.py
    │           │   │   ├── [01;34moperations[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── check.cpython-312.pyc
    │           │   │   │   │   ├── freeze.cpython-312.pyc
    │           │   │   │   │   └── prepare.cpython-312.pyc
    │           │   │   │   ├── [01;34mbuild[0m
    │           │   │   │   │   ├── __init__.py
    │           │   │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   │   ├── build_tracker.cpython-312.pyc
    │           │   │   │   │   │   ├── metadata.cpython-312.pyc
    │           │   │   │   │   │   ├── metadata_editable.cpython-312.pyc
    │           │   │   │   │   │   ├── wheel.cpython-312.pyc
    │           │   │   │   │   │   └── wheel_editable.cpython-312.pyc
    │           │   │   │   │   ├── build_tracker.py
    │           │   │   │   │   ├── metadata.py
    │           │   │   │   │   ├── metadata_editable.py
    │           │   │   │   │   ├── wheel.py
    │           │   │   │   │   └── wheel_editable.py
    │           │   │   │   ├── check.py
    │           │   │   │   ├── freeze.py
    │           │   │   │   ├── [01;34minstall[0m
    │           │   │   │   │   ├── __init__.py
    │           │   │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   │   └── wheel.cpython-312.pyc
    │           │   │   │   │   └── wheel.py
    │           │   │   │   └── prepare.py
    │           │   │   ├── pyproject.py
    │           │   │   ├── [01;34mreq[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── constructors.cpython-312.pyc
    │           │   │   │   │   ├── pep723.cpython-312.pyc
    │           │   │   │   │   ├── req_dependency_group.cpython-312.pyc
    │           │   │   │   │   ├── req_file.cpython-312.pyc
    │           │   │   │   │   ├── req_install.cpython-312.pyc
    │           │   │   │   │   ├── req_set.cpython-312.pyc
    │           │   │   │   │   └── req_uninstall.cpython-312.pyc
    │           │   │   │   ├── constructors.py
    │           │   │   │   ├── pep723.py
    │           │   │   │   ├── req_dependency_group.py
    │           │   │   │   ├── req_file.py
    │           │   │   │   ├── req_install.py
    │           │   │   │   ├── req_set.py
    │           │   │   │   └── req_uninstall.py
    │           │   │   ├── [01;34mresolution[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   └── base.cpython-312.pyc
    │           │   │   │   ├── base.py
    │           │   │   │   ├── [01;34mlegacy[0m
    │           │   │   │   │   ├── __init__.py
    │           │   │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   │   └── resolver.cpython-312.pyc
    │           │   │   │   │   └── resolver.py
    │           │   │   │   └── [01;34mresolvelib[0m
    │           │   │   │       ├── __init__.py
    │           │   │   │       ├── [01;34m__pycache__[0m
    │           │   │   │       │   ├── __init__.cpython-312.pyc
    │           │   │   │       │   ├── base.cpython-312.pyc
    │           │   │   │       │   ├── candidates.cpython-312.pyc
    │           │   │   │       │   ├── factory.cpython-312.pyc
    │           │   │   │       │   ├── found_candidates.cpython-312.pyc
    │           │   │   │       │   ├── provider.cpython-312.pyc
    │           │   │   │       │   ├── reporter.cpython-312.pyc
    │           │   │   │       │   ├── requirements.cpython-312.pyc
    │           │   │   │       │   └── resolver.cpython-312.pyc
    │           │   │   │       ├── base.py
    │           │   │   │       ├── candidates.py
    │           │   │   │       ├── factory.py
    │           │   │   │       ├── found_candidates.py
    │           │   │   │       ├── provider.py
    │           │   │   │       ├── reporter.py
    │           │   │   │       ├── requirements.py
    │           │   │   │       └── resolver.py
    │           │   │   ├── self_outdated_check.py
    │           │   │   ├── [01;34mutils[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── _jaraco_text.cpython-312.pyc
    │           │   │   │   │   ├── _log.cpython-312.pyc
    │           │   │   │   │   ├── appdirs.cpython-312.pyc
    │           │   │   │   │   ├── compat.cpython-312.pyc
    │           │   │   │   │   ├── compatibility_tags.cpython-312.pyc
    │           │   │   │   │   ├── datetime.cpython-312.pyc
    │           │   │   │   │   ├── deprecation.cpython-312.pyc
    │           │   │   │   │   ├── direct_url_helpers.cpython-312.pyc
    │           │   │   │   │   ├── egg_link.cpython-312.pyc
    │           │   │   │   │   ├── entrypoints.cpython-312.pyc
    │           │   │   │   │   ├── filesystem.cpython-312.pyc
    │           │   │   │   │   ├── filetypes.cpython-312.pyc
    │           │   │   │   │   ├── glibc.cpython-312.pyc
    │           │   │   │   │   ├── hashes.cpython-312.pyc
    │           │   │   │   │   ├── logging.cpython-312.pyc
    │           │   │   │   │   ├── misc.cpython-312.pyc
    │           │   │   │   │   ├── packaging.cpython-312.pyc
    │           │   │   │   │   ├── pylock.cpython-312.pyc
    │           │   │   │   │   ├── retry.cpython-312.pyc
    │           │   │   │   │   ├── subprocess.cpython-312.pyc
    │           │   │   │   │   ├── temp_dir.cpython-312.pyc
    │           │   │   │   │   ├── unpacking.cpython-312.pyc
    │           │   │   │   │   ├── urls.cpython-312.pyc
    │           │   │   │   │   ├── virtualenv.cpython-312.pyc
    │           │   │   │   │   └── wheel.cpython-312.pyc
    │           │   │   │   ├── _jaraco_text.py
    │           │   │   │   ├── _log.py
    │           │   │   │   ├── appdirs.py
    │           │   │   │   ├── compat.py
    │           │   │   │   ├── compatibility_tags.py
    │           │   │   │   ├── datetime.py
    │           │   │   │   ├── deprecation.py
    │           │   │   │   ├── direct_url_helpers.py
    │           │   │   │   ├── egg_link.py
    │           │   │   │   ├── entrypoints.py
    │           │   │   │   ├── filesystem.py
    │           │   │   │   ├── filetypes.py
    │           │   │   │   ├── glibc.py
    │           │   │   │   ├── hashes.py
    │           │   │   │   ├── logging.py
    │           │   │   │   ├── misc.py
    │           │   │   │   ├── packaging.py
    │           │   │   │   ├── pylock.py
    │           │   │   │   ├── retry.py
    │           │   │   │   ├── subprocess.py
    │           │   │   │   ├── temp_dir.py
    │           │   │   │   ├── unpacking.py
    │           │   │   │   ├── urls.py
    │           │   │   │   ├── virtualenv.py
    │           │   │   │   └── wheel.py
    │           │   │   ├── [01;34mvcs[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── bazaar.cpython-312.pyc
    │           │   │   │   │   ├── git.cpython-312.pyc
    │           │   │   │   │   ├── mercurial.cpython-312.pyc
    │           │   │   │   │   ├── subversion.cpython-312.pyc
    │           │   │   │   │   └── versioncontrol.cpython-312.pyc
    │           │   │   │   ├── bazaar.py
    │           │   │   │   ├── git.py
    │           │   │   │   ├── mercurial.py
    │           │   │   │   ├── subversion.py
    │           │   │   │   └── versioncontrol.py
    │           │   │   └── wheel_builder.py
    │           │   ├── [01;34m_vendor[0m
    │           │   │   ├── README.rst
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   └── __init__.cpython-312.pyc
    │           │   │   ├── [01;34mcachecontrol[0m
    │           │   │   │   ├── LICENSE.txt
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── _cmd.cpython-312.pyc
    │           │   │   │   │   ├── adapter.cpython-312.pyc
    │           │   │   │   │   ├── cache.cpython-312.pyc
    │           │   │   │   │   ├── controller.cpython-312.pyc
    │           │   │   │   │   ├── filewrapper.cpython-312.pyc
    │           │   │   │   │   ├── heuristics.cpython-312.pyc
    │           │   │   │   │   ├── serialize.cpython-312.pyc
    │           │   │   │   │   └── wrapper.cpython-312.pyc
    │           │   │   │   ├── _cmd.py
    │           │   │   │   ├── adapter.py
    │           │   │   │   ├── cache.py
    │           │   │   │   ├── [01;34mcaches[0m
    │           │   │   │   │   ├── __init__.py
    │           │   │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   │   ├── file_cache.cpython-312.pyc
    │           │   │   │   │   │   └── redis_cache.cpython-312.pyc
    │           │   │   │   │   ├── file_cache.py
    │           │   │   │   │   └── redis_cache.py
    │           │   │   │   ├── controller.py
    │           │   │   │   ├── filewrapper.py
    │           │   │   │   ├── heuristics.py
    │           │   │   │   ├── py.typed
    │           │   │   │   ├── serialize.py
    │           │   │   │   └── wrapper.py
    │           │   │   ├── [01;34mcertifi[0m
    │           │   │   │   ├── LICENSE
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── __main__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── __main__.cpython-312.pyc
    │           │   │   │   │   └── core.cpython-312.pyc
    │           │   │   │   ├── cacert.pem
    │           │   │   │   ├── core.py
    │           │   │   │   └── py.typed
    │           │   │   ├── [01;34mdependency_groups[0m
    │           │   │   │   ├── LICENSE.txt
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── __main__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── __main__.cpython-312.pyc
    │           │   │   │   │   ├── _implementation.cpython-312.pyc
    │           │   │   │   │   ├── _lint_dependency_groups.cpython-312.pyc
    │           │   │   │   │   ├── _pip_wrapper.cpython-312.pyc
    │           │   │   │   │   └── _toml_compat.cpython-312.pyc
    │           │   │   │   ├── _implementation.py
    │           │   │   │   ├── _lint_dependency_groups.py
    │           │   │   │   ├── _pip_wrapper.py
    │           │   │   │   ├── _toml_compat.py
    │           │   │   │   └── py.typed
    │           │   │   ├── [01;34mdistlib[0m
    │           │   │   │   ├── LICENSE.txt
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── compat.cpython-312.pyc
    │           │   │   │   │   ├── resources.cpython-312.pyc
    │           │   │   │   │   ├── scripts.cpython-312.pyc
    │           │   │   │   │   └── util.cpython-312.pyc
    │           │   │   │   ├── compat.py
    │           │   │   │   ├── resources.py
    │           │   │   │   ├── scripts.py
    │           │   │   │   ├── t32.exe
    │           │   │   │   ├── t64-arm.exe
    │           │   │   │   ├── t64.exe
    │           │   │   │   ├── util.py
    │           │   │   │   ├── w32.exe
    │           │   │   │   ├── w64-arm.exe
    │           │   │   │   └── w64.exe
    │           │   │   ├── [01;34mdistro[0m
    │           │   │   │   ├── LICENSE
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── __main__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── __main__.cpython-312.pyc
    │           │   │   │   │   └── distro.cpython-312.pyc
    │           │   │   │   ├── distro.py
    │           │   │   │   └── py.typed
    │           │   │   ├── [01;34midna[0m
    │           │   │   │   ├── LICENSE.md
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── codec.cpython-312.pyc
    │           │   │   │   │   ├── compat.cpython-312.pyc
    │           │   │   │   │   ├── core.cpython-312.pyc
    │           │   │   │   │   ├── idnadata.cpython-312.pyc
    │           │   │   │   │   ├── intranges.cpython-312.pyc
    │           │   │   │   │   ├── package_data.cpython-312.pyc
    │           │   │   │   │   └── uts46data.cpython-312.pyc
    │           │   │   │   ├── codec.py
    │           │   │   │   ├── compat.py
    │           │   │   │   ├── core.py
    │           │   │   │   ├── idnadata.py
    │           │   │   │   ├── intranges.py
    │           │   │   │   ├── package_data.py
    │           │   │   │   ├── py.typed
    │           │   │   │   └── uts46data.py
    │           │   │   ├── [01;34mmsgpack[0m
    │           │   │   │   ├── COPYING
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── exceptions.cpython-312.pyc
    │           │   │   │   │   ├── ext.cpython-312.pyc
    │           │   │   │   │   └── fallback.cpython-312.pyc
    │           │   │   │   ├── exceptions.py
    │           │   │   │   ├── ext.py
    │           │   │   │   └── fallback.py
    │           │   │   ├── [01;34mpackaging[0m
    │           │   │   │   ├── LICENSE
    │           │   │   │   ├── LICENSE.APACHE
    │           │   │   │   ├── LICENSE.BSD
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── _elffile.cpython-312.pyc
    │           │   │   │   │   ├── _manylinux.cpython-312.pyc
    │           │   │   │   │   ├── _musllinux.cpython-312.pyc
    │           │   │   │   │   ├── _parser.cpython-312.pyc
    │           │   │   │   │   ├── _structures.cpython-312.pyc
    │           │   │   │   │   ├── _tokenizer.cpython-312.pyc
    │           │   │   │   │   ├── markers.cpython-312.pyc
    │           │   │   │   │   ├── metadata.cpython-312.pyc
    │           │   │   │   │   ├── pylock.cpython-312.pyc
    │           │   │   │   │   ├── requirements.cpython-312.pyc
    │           │   │   │   │   ├── specifiers.cpython-312.pyc
    │           │   │   │   │   ├── tags.cpython-312.pyc
    │           │   │   │   │   ├── utils.cpython-312.pyc
    │           │   │   │   │   └── version.cpython-312.pyc
    │           │   │   │   ├── _elffile.py
    │           │   │   │   ├── _manylinux.py
    │           │   │   │   ├── _musllinux.py
    │           │   │   │   ├── _parser.py
    │           │   │   │   ├── _structures.py
    │           │   │   │   ├── _tokenizer.py
    │           │   │   │   ├── [01;34mlicenses[0m
    │           │   │   │   │   ├── __init__.py
    │           │   │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   │   └── _spdx.cpython-312.pyc
    │           │   │   │   │   └── _spdx.py
    │           │   │   │   ├── markers.py
    │           │   │   │   ├── metadata.py
    │           │   │   │   ├── py.typed
    │           │   │   │   ├── pylock.py
    │           │   │   │   ├── requirements.py
    │           │   │   │   ├── specifiers.py
    │           │   │   │   ├── tags.py
    │           │   │   │   ├── utils.py
    │           │   │   │   └── version.py
    │           │   │   ├── [01;34mpkg_resources[0m
    │           │   │   │   ├── LICENSE
    │           │   │   │   ├── __init__.py
    │           │   │   │   └── [01;34m__pycache__[0m
    │           │   │   │       └── __init__.cpython-312.pyc
    │           │   │   ├── [01;34mplatformdirs[0m
    │           │   │   │   ├── LICENSE
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── __main__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── __main__.cpython-312.pyc
    │           │   │   │   │   ├── android.cpython-312.pyc
    │           │   │   │   │   ├── api.cpython-312.pyc
    │           │   │   │   │   ├── macos.cpython-312.pyc
    │           │   │   │   │   ├── unix.cpython-312.pyc
    │           │   │   │   │   ├── version.cpython-312.pyc
    │           │   │   │   │   └── windows.cpython-312.pyc
    │           │   │   │   ├── android.py
    │           │   │   │   ├── api.py
    │           │   │   │   ├── macos.py
    │           │   │   │   ├── py.typed
    │           │   │   │   ├── unix.py
    │           │   │   │   ├── version.py
    │           │   │   │   └── windows.py
    │           │   │   ├── [01;34mpygments[0m
    │           │   │   │   ├── LICENSE
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── __main__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── __main__.cpython-312.pyc
    │           │   │   │   │   ├── console.cpython-312.pyc
    │           │   │   │   │   ├── filter.cpython-312.pyc
    │           │   │   │   │   ├── formatter.cpython-312.pyc
    │           │   │   │   │   ├── lexer.cpython-312.pyc
    │           │   │   │   │   ├── modeline.cpython-312.pyc
    │           │   │   │   │   ├── plugin.cpython-312.pyc
    │           │   │   │   │   ├── regexopt.cpython-312.pyc
    │           │   │   │   │   ├── scanner.cpython-312.pyc
    │           │   │   │   │   ├── sphinxext.cpython-312.pyc
    │           │   │   │   │   ├── style.cpython-312.pyc
    │           │   │   │   │   ├── token.cpython-312.pyc
    │           │   │   │   │   ├── unistring.cpython-312.pyc
    │           │   │   │   │   └── util.cpython-312.pyc
    │           │   │   │   ├── console.py
    │           │   │   │   ├── filter.py
    │           │   │   │   ├── [01;34mfilters[0m
    │           │   │   │   │   ├── __init__.py
    │           │   │   │   │   └── [01;34m__pycache__[0m
    │           │   │   │   │       └── __init__.cpython-312.pyc
    │           │   │   │   ├── formatter.py
    │           │   │   │   ├── [01;34mformatters[0m
    │           │   │   │   │   ├── __init__.py
    │           │   │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   │   └── _mapping.cpython-312.pyc
    │           │   │   │   │   └── _mapping.py
    │           │   │   │   ├── lexer.py
    │           │   │   │   ├── [01;34mlexers[0m
    │           │   │   │   │   ├── __init__.py
    │           │   │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   │   ├── _mapping.cpython-312.pyc
    │           │   │   │   │   │   └── python.cpython-312.pyc
    │           │   │   │   │   ├── _mapping.py
    │           │   │   │   │   └── python.py
    │           │   │   │   ├── modeline.py
    │           │   │   │   ├── plugin.py
    │           │   │   │   ├── regexopt.py
    │           │   │   │   ├── scanner.py
    │           │   │   │   ├── sphinxext.py
    │           │   │   │   ├── style.py
    │           │   │   │   ├── [01;34mstyles[0m
    │           │   │   │   │   ├── __init__.py
    │           │   │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   │   └── _mapping.cpython-312.pyc
    │           │   │   │   │   └── _mapping.py
    │           │   │   │   ├── token.py
    │           │   │   │   ├── unistring.py
    │           │   │   │   └── util.py
    │           │   │   ├── [01;34mpyproject_hooks[0m
    │           │   │   │   ├── LICENSE
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   └── _impl.cpython-312.pyc
    │           │   │   │   ├── _impl.py
    │           │   │   │   ├── [01;34m_in_process[0m
    │           │   │   │   │   ├── __init__.py
    │           │   │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   │   └── _in_process.cpython-312.pyc
    │           │   │   │   │   └── _in_process.py
    │           │   │   │   └── py.typed
    │           │   │   ├── [01;34mrequests[0m
    │           │   │   │   ├── LICENSE
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── __version__.cpython-312.pyc
    │           │   │   │   │   ├── _internal_utils.cpython-312.pyc
    │           │   │   │   │   ├── adapters.cpython-312.pyc
    │           │   │   │   │   ├── api.cpython-312.pyc
    │           │   │   │   │   ├── auth.cpython-312.pyc
    │           │   │   │   │   ├── certs.cpython-312.pyc
    │           │   │   │   │   ├── compat.cpython-312.pyc
    │           │   │   │   │   ├── cookies.cpython-312.pyc
    │           │   │   │   │   ├── exceptions.cpython-312.pyc
    │           │   │   │   │   ├── help.cpython-312.pyc
    │           │   │   │   │   ├── hooks.cpython-312.pyc
    │           │   │   │   │   ├── models.cpython-312.pyc
    │           │   │   │   │   ├── packages.cpython-312.pyc
    │           │   │   │   │   ├── sessions.cpython-312.pyc
    │           │   │   │   │   ├── status_codes.cpython-312.pyc
    │           │   │   │   │   ├── structures.cpython-312.pyc
    │           │   │   │   │   └── utils.cpython-312.pyc
    │           │   │   │   ├── __version__.py
    │           │   │   │   ├── _internal_utils.py
    │           │   │   │   ├── adapters.py
    │           │   │   │   ├── api.py
    │           │   │   │   ├── auth.py
    │           │   │   │   ├── certs.py
    │           │   │   │   ├── compat.py
    │           │   │   │   ├── cookies.py
    │           │   │   │   ├── exceptions.py
    │           │   │   │   ├── help.py
    │           │   │   │   ├── hooks.py
    │           │   │   │   ├── models.py
    │           │   │   │   ├── packages.py
    │           │   │   │   ├── sessions.py
    │           │   │   │   ├── status_codes.py
    │           │   │   │   ├── structures.py
    │           │   │   │   └── utils.py
    │           │   │   ├── [01;34mresolvelib[0m
    │           │   │   │   ├── LICENSE
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── providers.cpython-312.pyc
    │           │   │   │   │   ├── reporters.cpython-312.pyc
    │           │   │   │   │   └── structs.cpython-312.pyc
    │           │   │   │   ├── providers.py
    │           │   │   │   ├── py.typed
    │           │   │   │   ├── reporters.py
    │           │   │   │   ├── [01;34mresolvers[0m
    │           │   │   │   │   ├── __init__.py
    │           │   │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   │   ├── abstract.cpython-312.pyc
    │           │   │   │   │   │   ├── criterion.cpython-312.pyc
    │           │   │   │   │   │   ├── exceptions.cpython-312.pyc
    │           │   │   │   │   │   └── resolution.cpython-312.pyc
    │           │   │   │   │   ├── abstract.py
    │           │   │   │   │   ├── criterion.py
    │           │   │   │   │   ├── exceptions.py
    │           │   │   │   │   └── resolution.py
    │           │   │   │   └── structs.py
    │           │   │   ├── [01;34mrich[0m
    │           │   │   │   ├── LICENSE
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── __main__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── __main__.cpython-312.pyc
    │           │   │   │   │   ├── _cell_widths.cpython-312.pyc
    │           │   │   │   │   ├── _emoji_codes.cpython-312.pyc
    │           │   │   │   │   ├── _emoji_replace.cpython-312.pyc
    │           │   │   │   │   ├── _export_format.cpython-312.pyc
    │           │   │   │   │   ├── _extension.cpython-312.pyc
    │           │   │   │   │   ├── _fileno.cpython-312.pyc
    │           │   │   │   │   ├── _inspect.cpython-312.pyc
    │           │   │   │   │   ├── _log_render.cpython-312.pyc
    │           │   │   │   │   ├── _loop.cpython-312.pyc
    │           │   │   │   │   ├── _null_file.cpython-312.pyc
    │           │   │   │   │   ├── _palettes.cpython-312.pyc
    │           │   │   │   │   ├── _pick.cpython-312.pyc
    │           │   │   │   │   ├── _ratio.cpython-312.pyc
    │           │   │   │   │   ├── _spinners.cpython-312.pyc
    │           │   │   │   │   ├── _stack.cpython-312.pyc
    │           │   │   │   │   ├── _timer.cpython-312.pyc
    │           │   │   │   │   ├── _win32_console.cpython-312.pyc
    │           │   │   │   │   ├── _windows.cpython-312.pyc
    │           │   │   │   │   ├── _windows_renderer.cpython-312.pyc
    │           │   │   │   │   ├── _wrap.cpython-312.pyc
    │           │   │   │   │   ├── abc.cpython-312.pyc
    │           │   │   │   │   ├── align.cpython-312.pyc
    │           │   │   │   │   ├── ansi.cpython-312.pyc
    │           │   │   │   │   ├── bar.cpython-312.pyc
    │           │   │   │   │   ├── box.cpython-312.pyc
    │           │   │   │   │   ├── cells.cpython-312.pyc
    │           │   │   │   │   ├── color.cpython-312.pyc
    │           │   │   │   │   ├── color_triplet.cpython-312.pyc
    │           │   │   │   │   ├── columns.cpython-312.pyc
    │           │   │   │   │   ├── console.cpython-312.pyc
    │           │   │   │   │   ├── constrain.cpython-312.pyc
    │           │   │   │   │   ├── containers.cpython-312.pyc
    │           │   │   │   │   ├── control.cpython-312.pyc
    │           │   │   │   │   ├── default_styles.cpython-312.pyc
    │           │   │   │   │   ├── diagnose.cpython-312.pyc
    │           │   │   │   │   ├── emoji.cpython-312.pyc
    │           │   │   │   │   ├── errors.cpython-312.pyc
    │           │   │   │   │   ├── file_proxy.cpython-312.pyc
    │           │   │   │   │   ├── filesize.cpython-312.pyc
    │           │   │   │   │   ├── highlighter.cpython-312.pyc
    │           │   │   │   │   ├── json.cpython-312.pyc
    │           │   │   │   │   ├── jupyter.cpython-312.pyc
    │           │   │   │   │   ├── layout.cpython-312.pyc
    │           │   │   │   │   ├── live.cpython-312.pyc
    │           │   │   │   │   ├── live_render.cpython-312.pyc
    │           │   │   │   │   ├── logging.cpython-312.pyc
    │           │   │   │   │   ├── markup.cpython-312.pyc
    │           │   │   │   │   ├── measure.cpython-312.pyc
    │           │   │   │   │   ├── padding.cpython-312.pyc
    │           │   │   │   │   ├── pager.cpython-312.pyc
    │           │   │   │   │   ├── palette.cpython-312.pyc
    │           │   │   │   │   ├── panel.cpython-312.pyc
    │           │   │   │   │   ├── pretty.cpython-312.pyc
    │           │   │   │   │   ├── progress.cpython-312.pyc
    │           │   │   │   │   ├── progress_bar.cpython-312.pyc
    │           │   │   │   │   ├── prompt.cpython-312.pyc
    │           │   │   │   │   ├── protocol.cpython-312.pyc
    │           │   │   │   │   ├── region.cpython-312.pyc
    │           │   │   │   │   ├── repr.cpython-312.pyc
    │           │   │   │   │   ├── rule.cpython-312.pyc
    │           │   │   │   │   ├── scope.cpython-312.pyc
    │           │   │   │   │   ├── screen.cpython-312.pyc
    │           │   │   │   │   ├── segment.cpython-312.pyc
    │           │   │   │   │   ├── spinner.cpython-312.pyc
    │           │   │   │   │   ├── status.cpython-312.pyc
    │           │   │   │   │   ├── style.cpython-312.pyc
    │           │   │   │   │   ├── styled.cpython-312.pyc
    │           │   │   │   │   ├── syntax.cpython-312.pyc
    │           │   │   │   │   ├── table.cpython-312.pyc
    │           │   │   │   │   ├── terminal_theme.cpython-312.pyc
    │           │   │   │   │   ├── text.cpython-312.pyc
    │           │   │   │   │   ├── theme.cpython-312.pyc
    │           │   │   │   │   ├── themes.cpython-312.pyc
    │           │   │   │   │   ├── traceback.cpython-312.pyc
    │           │   │   │   │   └── tree.cpython-312.pyc
    │           │   │   │   ├── _cell_widths.py
    │           │   │   │   ├── _emoji_codes.py
    │           │   │   │   ├── _emoji_replace.py
    │           │   │   │   ├── _export_format.py
    │           │   │   │   ├── _extension.py
    │           │   │   │   ├── _fileno.py
    │           │   │   │   ├── _inspect.py
    │           │   │   │   ├── _log_render.py
    │           │   │   │   ├── _loop.py
    │           │   │   │   ├── _null_file.py
    │           │   │   │   ├── _palettes.py
    │           │   │   │   ├── _pick.py
    │           │   │   │   ├── _ratio.py
    │           │   │   │   ├── _spinners.py
    │           │   │   │   ├── _stack.py
    │           │   │   │   ├── _timer.py
    │           │   │   │   ├── _win32_console.py
    │           │   │   │   ├── _windows.py
    │           │   │   │   ├── _windows_renderer.py
    │           │   │   │   ├── _wrap.py
    │           │   │   │   ├── abc.py
    │           │   │   │   ├── align.py
    │           │   │   │   ├── ansi.py
    │           │   │   │   ├── bar.py
    │           │   │   │   ├── box.py
    │           │   │   │   ├── cells.py
    │           │   │   │   ├── color.py
    │           │   │   │   ├── color_triplet.py
    │           │   │   │   ├── columns.py
    │           │   │   │   ├── console.py
    │           │   │   │   ├── constrain.py
    │           │   │   │   ├── containers.py
    │           │   │   │   ├── control.py
    │           │   │   │   ├── default_styles.py
    │           │   │   │   ├── diagnose.py
    │           │   │   │   ├── emoji.py
    │           │   │   │   ├── errors.py
    │           │   │   │   ├── file_proxy.py
    │           │   │   │   ├── filesize.py
    │           │   │   │   ├── highlighter.py
    │           │   │   │   ├── json.py
    │           │   │   │   ├── jupyter.py
    │           │   │   │   ├── layout.py
    │           │   │   │   ├── live.py
    │           │   │   │   ├── live_render.py
    │           │   │   │   ├── logging.py
    │           │   │   │   ├── markup.py
    │           │   │   │   ├── measure.py
    │           │   │   │   ├── padding.py
    │           │   │   │   ├── pager.py
    │           │   │   │   ├── palette.py
    │           │   │   │   ├── panel.py
    │           │   │   │   ├── pretty.py
    │           │   │   │   ├── progress.py
    │           │   │   │   ├── progress_bar.py
    │           │   │   │   ├── prompt.py
    │           │   │   │   ├── protocol.py
    │           │   │   │   ├── py.typed
    │           │   │   │   ├── region.py
    │           │   │   │   ├── repr.py
    │           │   │   │   ├── rule.py
    │           │   │   │   ├── scope.py
    │           │   │   │   ├── screen.py
    │           │   │   │   ├── segment.py
    │           │   │   │   ├── spinner.py
    │           │   │   │   ├── status.py
    │           │   │   │   ├── style.py
    │           │   │   │   ├── styled.py
    │           │   │   │   ├── syntax.py
    │           │   │   │   ├── table.py
    │           │   │   │   ├── terminal_theme.py
    │           │   │   │   ├── text.py
    │           │   │   │   ├── theme.py
    │           │   │   │   ├── themes.py
    │           │   │   │   ├── traceback.py
    │           │   │   │   └── tree.py
    │           │   │   ├── [01;34mtomli[0m
    │           │   │   │   ├── LICENSE
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── _parser.cpython-312.pyc
    │           │   │   │   │   ├── _re.cpython-312.pyc
    │           │   │   │   │   └── _types.cpython-312.pyc
    │           │   │   │   ├── _parser.py
    │           │   │   │   ├── _re.py
    │           │   │   │   ├── _types.py
    │           │   │   │   └── py.typed
    │           │   │   ├── [01;34mtomli_w[0m
    │           │   │   │   ├── LICENSE
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   └── _writer.cpython-312.pyc
    │           │   │   │   ├── _writer.py
    │           │   │   │   └── py.typed
    │           │   │   ├── [01;34mtruststore[0m
    │           │   │   │   ├── LICENSE
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── _api.cpython-312.pyc
    │           │   │   │   │   ├── _macos.cpython-312.pyc
    │           │   │   │   │   ├── _openssl.cpython-312.pyc
    │           │   │   │   │   ├── _ssl_constants.cpython-312.pyc
    │           │   │   │   │   └── _windows.cpython-312.pyc
    │           │   │   │   ├── _api.py
    │           │   │   │   ├── _macos.py
    │           │   │   │   ├── _openssl.py
    │           │   │   │   ├── _ssl_constants.py
    │           │   │   │   ├── _windows.py
    │           │   │   │   └── py.typed
    │           │   │   ├── [01;34murllib3[0m
    │           │   │   │   ├── LICENSE.txt
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── _collections.cpython-312.pyc
    │           │   │   │   │   ├── _version.cpython-312.pyc
    │           │   │   │   │   ├── connection.cpython-312.pyc
    │           │   │   │   │   ├── connectionpool.cpython-312.pyc
    │           │   │   │   │   ├── exceptions.cpython-312.pyc
    │           │   │   │   │   ├── fields.cpython-312.pyc
    │           │   │   │   │   ├── filepost.cpython-312.pyc
    │           │   │   │   │   ├── poolmanager.cpython-312.pyc
    │           │   │   │   │   ├── request.cpython-312.pyc
    │           │   │   │   │   └── response.cpython-312.pyc
    │           │   │   │   ├── _collections.py
    │           │   │   │   ├── _version.py
    │           │   │   │   ├── connection.py
    │           │   │   │   ├── connectionpool.py
    │           │   │   │   ├── [01;34mcontrib[0m
    │           │   │   │   │   ├── __init__.py
    │           │   │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   │   ├── _appengine_environ.cpython-312.pyc
    │           │   │   │   │   │   ├── appengine.cpython-312.pyc
    │           │   │   │   │   │   ├── ntlmpool.cpython-312.pyc
    │           │   │   │   │   │   ├── pyopenssl.cpython-312.pyc
    │           │   │   │   │   │   ├── securetransport.cpython-312.pyc
    │           │   │   │   │   │   └── socks.cpython-312.pyc
    │           │   │   │   │   ├── _appengine_environ.py
    │           │   │   │   │   ├── [01;34m_securetransport[0m
    │           │   │   │   │   │   ├── __init__.py
    │           │   │   │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   │   │   ├── bindings.cpython-312.pyc
    │           │   │   │   │   │   │   └── low_level.cpython-312.pyc
    │           │   │   │   │   │   ├── bindings.py
    │           │   │   │   │   │   └── low_level.py
    │           │   │   │   │   ├── appengine.py
    │           │   │   │   │   ├── ntlmpool.py
    │           │   │   │   │   ├── pyopenssl.py
    │           │   │   │   │   ├── securetransport.py
    │           │   │   │   │   └── socks.py
    │           │   │   │   ├── exceptions.py
    │           │   │   │   ├── fields.py
    │           │   │   │   ├── filepost.py
    │           │   │   │   ├── [01;34mpackages[0m
    │           │   │   │   │   ├── __init__.py
    │           │   │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   │   └── six.cpython-312.pyc
    │           │   │   │   │   ├── [01;34mbackports[0m
    │           │   │   │   │   │   ├── __init__.py
    │           │   │   │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   │   │   ├── makefile.cpython-312.pyc
    │           │   │   │   │   │   │   └── weakref_finalize.cpython-312.pyc
    │           │   │   │   │   │   ├── makefile.py
    │           │   │   │   │   │   └── weakref_finalize.py
    │           │   │   │   │   └── six.py
    │           │   │   │   ├── poolmanager.py
    │           │   │   │   ├── request.py
    │           │   │   │   ├── response.py
    │           │   │   │   └── [01;34mutil[0m
    │           │   │   │       ├── __init__.py
    │           │   │   │       ├── [01;34m__pycache__[0m
    │           │   │   │       │   ├── __init__.cpython-312.pyc
    │           │   │   │       │   ├── connection.cpython-312.pyc
    │           │   │   │       │   ├── proxy.cpython-312.pyc
    │           │   │   │       │   ├── queue.cpython-312.pyc
    │           │   │   │       │   ├── request.cpython-312.pyc
    │           │   │   │       │   ├── response.cpython-312.pyc
    │           │   │   │       │   ├── retry.cpython-312.pyc
    │           │   │   │       │   ├── ssl_.cpython-312.pyc
    │           │   │   │       │   ├── ssl_match_hostname.cpython-312.pyc
    │           │   │   │       │   ├── ssltransport.cpython-312.pyc
    │           │   │   │       │   ├── timeout.cpython-312.pyc
    │           │   │   │       │   ├── url.cpython-312.pyc
    │           │   │   │       │   └── wait.cpython-312.pyc
    │           │   │   │       ├── connection.py
    │           │   │   │       ├── proxy.py
    │           │   │   │       ├── queue.py
    │           │   │   │       ├── request.py
    │           │   │   │       ├── response.py
    │           │   │   │       ├── retry.py
    │           │   │   │       ├── ssl_.py
    │           │   │   │       ├── ssl_match_hostname.py
    │           │   │   │       ├── ssltransport.py
    │           │   │   │       ├── timeout.py
    │           │   │   │       ├── url.py
    │           │   │   │       └── wait.py
    │           │   │   └── vendor.txt
    │           │   └── py.typed
    │           ├── [01;34mpip-26.0.1.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── REQUESTED
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   └── [01;34mlicenses[0m
    │           │       ├── AUTHORS.txt
    │           │       ├── LICENSE.txt
    │           │       └── [01;34msrc[0m
    │           │           └── [01;34mpip[0m
    │           │               └── [01;34m_vendor[0m
    │           │                   ├── [01;34mcachecontrol[0m
    │           │                   │   └── LICENSE.txt
    │           │                   ├── [01;34mcertifi[0m
    │           │                   │   └── LICENSE
    │           │                   ├── [01;34mdependency_groups[0m
    │           │                   │   └── LICENSE.txt
    │           │                   ├── [01;34mdistlib[0m
    │           │                   │   └── LICENSE.txt
    │           │                   ├── [01;34mdistro[0m
    │           │                   │   └── LICENSE
    │           │                   ├── [01;34midna[0m
    │           │                   │   └── LICENSE.md
    │           │                   ├── [01;34mmsgpack[0m
    │           │                   │   └── COPYING
    │           │                   ├── [01;34mpackaging[0m
    │           │                   │   ├── LICENSE
    │           │                   │   ├── LICENSE.APACHE
    │           │                   │   └── LICENSE.BSD
    │           │                   ├── [01;34mpkg_resources[0m
    │           │                   │   └── LICENSE
    │           │                   ├── [01;34mplatformdirs[0m
    │           │                   │   └── LICENSE
    │           │                   ├── [01;34mpygments[0m
    │           │                   │   └── LICENSE
    │           │                   ├── [01;34mpyproject_hooks[0m
    │           │                   │   └── LICENSE
    │           │                   ├── [01;34mrequests[0m
    │           │                   │   └── LICENSE
    │           │                   ├── [01;34mresolvelib[0m
    │           │                   │   └── LICENSE
    │           │                   ├── [01;34mrich[0m
    │           │                   │   └── LICENSE
    │           │                   ├── [01;34mtomli[0m
    │           │                   │   └── LICENSE
    │           │                   ├── [01;34mtomli_w[0m
    │           │                   │   └── LICENSE
    │           │                   ├── [01;34mtruststore[0m
    │           │                   │   └── LICENSE
    │           │                   └── [01;34murllib3[0m
    │           │                       └── LICENSE.txt
    │           ├── [01;34mpluggy[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── _callers.cpython-312.pyc
    │           │   │   ├── _hooks.cpython-312.pyc
    │           │   │   ├── _manager.cpython-312.pyc
    │           │   │   ├── _result.cpython-312.pyc
    │           │   │   ├── _tracing.cpython-312.pyc
    │           │   │   ├── _version.cpython-312.pyc
    │           │   │   └── _warnings.cpython-312.pyc
    │           │   ├── _callers.py
    │           │   ├── _hooks.py
    │           │   ├── _manager.py
    │           │   ├── _result.py
    │           │   ├── _tracing.py
    │           │   ├── _version.py
    │           │   ├── _warnings.py
    │           │   └── py.typed
    │           ├── [01;34mpluggy-1.6.0.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   ├── [01;34mlicenses[0m
    │           │   │   └── LICENSE
    │           │   └── top_level.txt
    │           ├── py.py
    │           ├── [01;34mpydantic[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── _migration.cpython-312.pyc
    │           │   │   ├── alias_generators.cpython-312.pyc
    │           │   │   ├── aliases.cpython-312.pyc
    │           │   │   ├── annotated_handlers.cpython-312.pyc
    │           │   │   ├── class_validators.cpython-312.pyc
    │           │   │   ├── color.cpython-312.pyc
    │           │   │   ├── config.cpython-312.pyc
    │           │   │   ├── dataclasses.cpython-312.pyc
    │           │   │   ├── datetime_parse.cpython-312.pyc
    │           │   │   ├── decorator.cpython-312.pyc
    │           │   │   ├── env_settings.cpython-312.pyc
    │           │   │   ├── error_wrappers.cpython-312.pyc
    │           │   │   ├── errors.cpython-312.pyc
    │           │   │   ├── fields.cpython-312.pyc
    │           │   │   ├── functional_serializers.cpython-312.pyc
    │           │   │   ├── functional_validators.cpython-312.pyc
    │           │   │   ├── generics.cpython-312.pyc
    │           │   │   ├── json.cpython-312.pyc
    │           │   │   ├── json_schema.cpython-312.pyc
    │           │   │   ├── main.cpython-312.pyc
    │           │   │   ├── mypy.cpython-312.pyc
    │           │   │   ├── networks.cpython-312.pyc
    │           │   │   ├── parse.cpython-312.pyc
    │           │   │   ├── root_model.cpython-312.pyc
    │           │   │   ├── schema.cpython-312.pyc
    │           │   │   ├── tools.cpython-312.pyc
    │           │   │   ├── type_adapter.cpython-312.pyc
    │           │   │   ├── types.cpython-312.pyc
    │           │   │   ├── typing.cpython-312.pyc
    │           │   │   ├── utils.cpython-312.pyc
    │           │   │   ├── validate_call_decorator.cpython-312.pyc
    │           │   │   ├── validators.cpython-312.pyc
    │           │   │   ├── version.cpython-312.pyc
    │           │   │   └── warnings.cpython-312.pyc
    │           │   ├── [01;34m_internal[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── _config.cpython-312.pyc
    │           │   │   │   ├── _core_metadata.cpython-312.pyc
    │           │   │   │   ├── _core_utils.cpython-312.pyc
    │           │   │   │   ├── _dataclasses.cpython-312.pyc
    │           │   │   │   ├── _decorators.cpython-312.pyc
    │           │   │   │   ├── _decorators_v1.cpython-312.pyc
    │           │   │   │   ├── _discriminated_union.cpython-312.pyc
    │           │   │   │   ├── _docs_extraction.cpython-312.pyc
    │           │   │   │   ├── _fields.cpython-312.pyc
    │           │   │   │   ├── _forward_ref.cpython-312.pyc
    │           │   │   │   ├── _generate_schema.cpython-312.pyc
    │           │   │   │   ├── _generics.cpython-312.pyc
    │           │   │   │   ├── _git.cpython-312.pyc
    │           │   │   │   ├── _import_utils.cpython-312.pyc
    │           │   │   │   ├── _internal_dataclass.cpython-312.pyc
    │           │   │   │   ├── _known_annotated_metadata.cpython-312.pyc
    │           │   │   │   ├── _mock_val_ser.cpython-312.pyc
    │           │   │   │   ├── _model_construction.cpython-312.pyc
    │           │   │   │   ├── _namespace_utils.cpython-312.pyc
    │           │   │   │   ├── _repr.cpython-312.pyc
    │           │   │   │   ├── _schema_gather.cpython-312.pyc
    │           │   │   │   ├── _schema_generation_shared.cpython-312.pyc
    │           │   │   │   ├── _serializers.cpython-312.pyc
    │           │   │   │   ├── _signature.cpython-312.pyc
    │           │   │   │   ├── _typing_extra.cpython-312.pyc
    │           │   │   │   ├── _utils.cpython-312.pyc
    │           │   │   │   ├── _validate_call.cpython-312.pyc
    │           │   │   │   └── _validators.cpython-312.pyc
    │           │   │   ├── _config.py
    │           │   │   ├── _core_metadata.py
    │           │   │   ├── _core_utils.py
    │           │   │   ├── _dataclasses.py
    │           │   │   ├── _decorators.py
    │           │   │   ├── _decorators_v1.py
    │           │   │   ├── _discriminated_union.py
    │           │   │   ├── _docs_extraction.py
    │           │   │   ├── _fields.py
    │           │   │   ├── _forward_ref.py
    │           │   │   ├── _generate_schema.py
    │           │   │   ├── _generics.py
    │           │   │   ├── _git.py
    │           │   │   ├── _import_utils.py
    │           │   │   ├── _internal_dataclass.py
    │           │   │   ├── _known_annotated_metadata.py
    │           │   │   ├── _mock_val_ser.py
    │           │   │   ├── _model_construction.py
    │           │   │   ├── _namespace_utils.py
    │           │   │   ├── _repr.py
    │           │   │   ├── _schema_gather.py
    │           │   │   ├── _schema_generation_shared.py
    │           │   │   ├── _serializers.py
    │           │   │   ├── _signature.py
    │           │   │   ├── _typing_extra.py
    │           │   │   ├── _utils.py
    │           │   │   ├── _validate_call.py
    │           │   │   └── _validators.py
    │           │   ├── _migration.py
    │           │   ├── alias_generators.py
    │           │   ├── aliases.py
    │           │   ├── annotated_handlers.py
    │           │   ├── class_validators.py
    │           │   ├── color.py
    │           │   ├── config.py
    │           │   ├── dataclasses.py
    │           │   ├── datetime_parse.py
    │           │   ├── decorator.py
    │           │   ├── [01;34mdeprecated[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── class_validators.cpython-312.pyc
    │           │   │   │   ├── config.cpython-312.pyc
    │           │   │   │   ├── copy_internals.cpython-312.pyc
    │           │   │   │   ├── decorator.cpython-312.pyc
    │           │   │   │   ├── json.cpython-312.pyc
    │           │   │   │   ├── parse.cpython-312.pyc
    │           │   │   │   └── tools.cpython-312.pyc
    │           │   │   ├── class_validators.py
    │           │   │   ├── config.py
    │           │   │   ├── copy_internals.py
    │           │   │   ├── decorator.py
    │           │   │   ├── json.py
    │           │   │   ├── parse.py
    │           │   │   └── tools.py
    │           │   ├── env_settings.py
    │           │   ├── error_wrappers.py
    │           │   ├── errors.py
    │           │   ├── [01;34mexperimental[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── arguments_schema.cpython-312.pyc
    │           │   │   │   ├── missing_sentinel.cpython-312.pyc
    │           │   │   │   └── pipeline.cpython-312.pyc
    │           │   │   ├── arguments_schema.py
    │           │   │   ├── missing_sentinel.py
    │           │   │   └── pipeline.py
    │           │   ├── fields.py
    │           │   ├── functional_serializers.py
    │           │   ├── functional_validators.py
    │           │   ├── generics.py
    │           │   ├── json.py
    │           │   ├── json_schema.py
    │           │   ├── main.py
    │           │   ├── mypy.py
    │           │   ├── networks.py
    │           │   ├── parse.py
    │           │   ├── [01;34mplugin[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── _loader.cpython-312.pyc
    │           │   │   │   └── _schema_validator.cpython-312.pyc
    │           │   │   ├── _loader.py
    │           │   │   └── _schema_validator.py
    │           │   ├── py.typed
    │           │   ├── root_model.py
    │           │   ├── schema.py
    │           │   ├── tools.py
    │           │   ├── type_adapter.py
    │           │   ├── types.py
    │           │   ├── typing.py
    │           │   ├── utils.py
    │           │   ├── [01;34mv1[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── _hypothesis_plugin.cpython-312.pyc
    │           │   │   │   ├── annotated_types.cpython-312.pyc
    │           │   │   │   ├── class_validators.cpython-312.pyc
    │           │   │   │   ├── color.cpython-312.pyc
    │           │   │   │   ├── config.cpython-312.pyc
    │           │   │   │   ├── dataclasses.cpython-312.pyc
    │           │   │   │   ├── datetime_parse.cpython-312.pyc
    │           │   │   │   ├── decorator.cpython-312.pyc
    │           │   │   │   ├── env_settings.cpython-312.pyc
    │           │   │   │   ├── error_wrappers.cpython-312.pyc
    │           │   │   │   ├── errors.cpython-312.pyc
    │           │   │   │   ├── fields.cpython-312.pyc
    │           │   │   │   ├── generics.cpython-312.pyc
    │           │   │   │   ├── json.cpython-312.pyc
    │           │   │   │   ├── main.cpython-312.pyc
    │           │   │   │   ├── mypy.cpython-312.pyc
    │           │   │   │   ├── networks.cpython-312.pyc
    │           │   │   │   ├── parse.cpython-312.pyc
    │           │   │   │   ├── schema.cpython-312.pyc
    │           │   │   │   ├── tools.cpython-312.pyc
    │           │   │   │   ├── types.cpython-312.pyc
    │           │   │   │   ├── typing.cpython-312.pyc
    │           │   │   │   ├── utils.cpython-312.pyc
    │           │   │   │   ├── validators.cpython-312.pyc
    │           │   │   │   └── version.cpython-312.pyc
    │           │   │   ├── _hypothesis_plugin.py
    │           │   │   ├── annotated_types.py
    │           │   │   ├── class_validators.py
    │           │   │   ├── color.py
    │           │   │   ├── config.py
    │           │   │   ├── dataclasses.py
    │           │   │   ├── datetime_parse.py
    │           │   │   ├── decorator.py
    │           │   │   ├── env_settings.py
    │           │   │   ├── error_wrappers.py
    │           │   │   ├── errors.py
    │           │   │   ├── fields.py
    │           │   │   ├── generics.py
    │           │   │   ├── json.py
    │           │   │   ├── main.py
    │           │   │   ├── mypy.py
    │           │   │   ├── networks.py
    │           │   │   ├── parse.py
    │           │   │   ├── py.typed
    │           │   │   ├── schema.py
    │           │   │   ├── tools.py
    │           │   │   ├── types.py
    │           │   │   ├── typing.py
    │           │   │   ├── utils.py
    │           │   │   ├── validators.py
    │           │   │   └── version.py
    │           │   ├── validate_call_decorator.py
    │           │   ├── validators.py
    │           │   ├── version.py
    │           │   └── warnings.py
    │           ├── [01;34mpydantic-2.12.5.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── REQUESTED
    │           │   ├── WHEEL
    │           │   └── [01;34mlicenses[0m
    │           │       └── LICENSE
    │           ├── [01;34mpydantic_core[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   └── core_schema.cpython-312.pyc
    │           │   ├── [01;32m_pydantic_core.cpython-312-x86_64-linux-gnu.so[0m
    │           │   ├── _pydantic_core.pyi
    │           │   ├── core_schema.py
    │           │   └── py.typed
    │           ├── [01;34mpydantic_core-2.41.5.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── [01;34mlicenses[0m
    │           │       └── LICENSE
    │           ├── [01;34mpygments[0m
    │           │   ├── __init__.py
    │           │   ├── __main__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── __main__.cpython-312.pyc
    │           │   │   ├── cmdline.cpython-312.pyc
    │           │   │   ├── console.cpython-312.pyc
    │           │   │   ├── filter.cpython-312.pyc
    │           │   │   ├── formatter.cpython-312.pyc
    │           │   │   ├── lexer.cpython-312.pyc
    │           │   │   ├── modeline.cpython-312.pyc
    │           │   │   ├── plugin.cpython-312.pyc
    │           │   │   ├── regexopt.cpython-312.pyc
    │           │   │   ├── scanner.cpython-312.pyc
    │           │   │   ├── sphinxext.cpython-312.pyc
    │           │   │   ├── style.cpython-312.pyc
    │           │   │   ├── token.cpython-312.pyc
    │           │   │   ├── unistring.cpython-312.pyc
    │           │   │   └── util.cpython-312.pyc
    │           │   ├── cmdline.py
    │           │   ├── console.py
    │           │   ├── filter.py
    │           │   ├── [01;34mfilters[0m
    │           │   │   ├── __init__.py
    │           │   │   └── [01;34m__pycache__[0m
    │           │   │       └── __init__.cpython-312.pyc
    │           │   ├── formatter.py
    │           │   ├── [01;34mformatters[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── _mapping.cpython-312.pyc
    │           │   │   │   ├── bbcode.cpython-312.pyc
    │           │   │   │   ├── groff.cpython-312.pyc
    │           │   │   │   ├── html.cpython-312.pyc
    │           │   │   │   ├── img.cpython-312.pyc
    │           │   │   │   ├── irc.cpython-312.pyc
    │           │   │   │   ├── latex.cpython-312.pyc
    │           │   │   │   ├── other.cpython-312.pyc
    │           │   │   │   ├── pangomarkup.cpython-312.pyc
    │           │   │   │   ├── rtf.cpython-312.pyc
    │           │   │   │   ├── svg.cpython-312.pyc
    │           │   │   │   ├── terminal.cpython-312.pyc
    │           │   │   │   └── terminal256.cpython-312.pyc
    │           │   │   ├── _mapping.py
    │           │   │   ├── bbcode.py
    │           │   │   ├── groff.py
    │           │   │   ├── html.py
    │           │   │   ├── img.py
    │           │   │   ├── irc.py
    │           │   │   ├── latex.py
    │           │   │   ├── other.py
    │           │   │   ├── pangomarkup.py
    │           │   │   ├── rtf.py
    │           │   │   ├── svg.py
    │           │   │   ├── terminal.py
    │           │   │   └── terminal256.py
    │           │   ├── lexer.py
    │           │   ├── [01;34mlexers[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── _ada_builtins.cpython-312.pyc
    │           │   │   │   ├── _asy_builtins.cpython-312.pyc
    │           │   │   │   ├── _cl_builtins.cpython-312.pyc
    │           │   │   │   ├── _cocoa_builtins.cpython-312.pyc
    │           │   │   │   ├── _csound_builtins.cpython-312.pyc
    │           │   │   │   ├── _css_builtins.cpython-312.pyc
    │           │   │   │   ├── _googlesql_builtins.cpython-312.pyc
    │           │   │   │   ├── _julia_builtins.cpython-312.pyc
    │           │   │   │   ├── _lasso_builtins.cpython-312.pyc
    │           │   │   │   ├── _lilypond_builtins.cpython-312.pyc
    │           │   │   │   ├── _lua_builtins.cpython-312.pyc
    │           │   │   │   ├── _luau_builtins.cpython-312.pyc
    │           │   │   │   ├── _mapping.cpython-312.pyc
    │           │   │   │   ├── _mql_builtins.cpython-312.pyc
    │           │   │   │   ├── _mysql_builtins.cpython-312.pyc
    │           │   │   │   ├── _openedge_builtins.cpython-312.pyc
    │           │   │   │   ├── _php_builtins.cpython-312.pyc
    │           │   │   │   ├── _postgres_builtins.cpython-312.pyc
    │           │   │   │   ├── _qlik_builtins.cpython-312.pyc
    │           │   │   │   ├── _scheme_builtins.cpython-312.pyc
    │           │   │   │   ├── _scilab_builtins.cpython-312.pyc
    │           │   │   │   ├── _sourcemod_builtins.cpython-312.pyc
    │           │   │   │   ├── _sql_builtins.cpython-312.pyc
    │           │   │   │   ├── _stan_builtins.cpython-312.pyc
    │           │   │   │   ├── _stata_builtins.cpython-312.pyc
    │           │   │   │   ├── _tsql_builtins.cpython-312.pyc
    │           │   │   │   ├── _usd_builtins.cpython-312.pyc
    │           │   │   │   ├── _vbscript_builtins.cpython-312.pyc
    │           │   │   │   ├── _vim_builtins.cpython-312.pyc
    │           │   │   │   ├── actionscript.cpython-312.pyc
    │           │   │   │   ├── ada.cpython-312.pyc
    │           │   │   │   ├── agile.cpython-312.pyc
    │           │   │   │   ├── algebra.cpython-312.pyc
    │           │   │   │   ├── ambient.cpython-312.pyc
    │           │   │   │   ├── amdgpu.cpython-312.pyc
    │           │   │   │   ├── ampl.cpython-312.pyc
    │           │   │   │   ├── apdlexer.cpython-312.pyc
    │           │   │   │   ├── apl.cpython-312.pyc
    │           │   │   │   ├── archetype.cpython-312.pyc
    │           │   │   │   ├── arrow.cpython-312.pyc
    │           │   │   │   ├── arturo.cpython-312.pyc
    │           │   │   │   ├── asc.cpython-312.pyc
    │           │   │   │   ├── asm.cpython-312.pyc
    │           │   │   │   ├── asn1.cpython-312.pyc
    │           │   │   │   ├── automation.cpython-312.pyc
    │           │   │   │   ├── bare.cpython-312.pyc
    │           │   │   │   ├── basic.cpython-312.pyc
    │           │   │   │   ├── bdd.cpython-312.pyc
    │           │   │   │   ├── berry.cpython-312.pyc
    │           │   │   │   ├── bibtex.cpython-312.pyc
    │           │   │   │   ├── blueprint.cpython-312.pyc
    │           │   │   │   ├── boa.cpython-312.pyc
    │           │   │   │   ├── bqn.cpython-312.pyc
    │           │   │   │   ├── business.cpython-312.pyc
    │           │   │   │   ├── c_cpp.cpython-312.pyc
    │           │   │   │   ├── c_like.cpython-312.pyc
    │           │   │   │   ├── capnproto.cpython-312.pyc
    │           │   │   │   ├── carbon.cpython-312.pyc
    │           │   │   │   ├── cddl.cpython-312.pyc
    │           │   │   │   ├── chapel.cpython-312.pyc
    │           │   │   │   ├── clean.cpython-312.pyc
    │           │   │   │   ├── codeql.cpython-312.pyc
    │           │   │   │   ├── comal.cpython-312.pyc
    │           │   │   │   ├── compiled.cpython-312.pyc
    │           │   │   │   ├── configs.cpython-312.pyc
    │           │   │   │   ├── console.cpython-312.pyc
    │           │   │   │   ├── cplint.cpython-312.pyc
    │           │   │   │   ├── crystal.cpython-312.pyc
    │           │   │   │   ├── csound.cpython-312.pyc
    │           │   │   │   ├── css.cpython-312.pyc
    │           │   │   │   ├── d.cpython-312.pyc
    │           │   │   │   ├── dalvik.cpython-312.pyc
    │           │   │   │   ├── data.cpython-312.pyc
    │           │   │   │   ├── dax.cpython-312.pyc
    │           │   │   │   ├── devicetree.cpython-312.pyc
    │           │   │   │   ├── diff.cpython-312.pyc
    │           │   │   │   ├── dns.cpython-312.pyc
    │           │   │   │   ├── dotnet.cpython-312.pyc
    │           │   │   │   ├── dsls.cpython-312.pyc
    │           │   │   │   ├── dylan.cpython-312.pyc
    │           │   │   │   ├── ecl.cpython-312.pyc
    │           │   │   │   ├── eiffel.cpython-312.pyc
    │           │   │   │   ├── elm.cpython-312.pyc
    │           │   │   │   ├── elpi.cpython-312.pyc
    │           │   │   │   ├── email.cpython-312.pyc
    │           │   │   │   ├── erlang.cpython-312.pyc
    │           │   │   │   ├── esoteric.cpython-312.pyc
    │           │   │   │   ├── ezhil.cpython-312.pyc
    │           │   │   │   ├── factor.cpython-312.pyc
    │           │   │   │   ├── fantom.cpython-312.pyc
    │           │   │   │   ├── felix.cpython-312.pyc
    │           │   │   │   ├── fift.cpython-312.pyc
    │           │   │   │   ├── floscript.cpython-312.pyc
    │           │   │   │   ├── forth.cpython-312.pyc
    │           │   │   │   ├── fortran.cpython-312.pyc
    │           │   │   │   ├── foxpro.cpython-312.pyc
    │           │   │   │   ├── freefem.cpython-312.pyc
    │           │   │   │   ├── func.cpython-312.pyc
    │           │   │   │   ├── functional.cpython-312.pyc
    │           │   │   │   ├── futhark.cpython-312.pyc
    │           │   │   │   ├── gcodelexer.cpython-312.pyc
    │           │   │   │   ├── gdscript.cpython-312.pyc
    │           │   │   │   ├── gleam.cpython-312.pyc
    │           │   │   │   ├── go.cpython-312.pyc
    │           │   │   │   ├── grammar_notation.cpython-312.pyc
    │           │   │   │   ├── graph.cpython-312.pyc
    │           │   │   │   ├── graphics.cpython-312.pyc
    │           │   │   │   ├── graphql.cpython-312.pyc
    │           │   │   │   ├── graphviz.cpython-312.pyc
    │           │   │   │   ├── gsql.cpython-312.pyc
    │           │   │   │   ├── hare.cpython-312.pyc
    │           │   │   │   ├── haskell.cpython-312.pyc
    │           │   │   │   ├── haxe.cpython-312.pyc
    │           │   │   │   ├── hdl.cpython-312.pyc
    │           │   │   │   ├── hexdump.cpython-312.pyc
    │           │   │   │   ├── html.cpython-312.pyc
    │           │   │   │   ├── idl.cpython-312.pyc
    │           │   │   │   ├── igor.cpython-312.pyc
    │           │   │   │   ├── inferno.cpython-312.pyc
    │           │   │   │   ├── installers.cpython-312.pyc
    │           │   │   │   ├── int_fiction.cpython-312.pyc
    │           │   │   │   ├── iolang.cpython-312.pyc
    │           │   │   │   ├── j.cpython-312.pyc
    │           │   │   │   ├── javascript.cpython-312.pyc
    │           │   │   │   ├── jmespath.cpython-312.pyc
    │           │   │   │   ├── jslt.cpython-312.pyc
    │           │   │   │   ├── json5.cpython-312.pyc
    │           │   │   │   ├── jsonnet.cpython-312.pyc
    │           │   │   │   ├── jsx.cpython-312.pyc
    │           │   │   │   ├── julia.cpython-312.pyc
    │           │   │   │   ├── jvm.cpython-312.pyc
    │           │   │   │   ├── kuin.cpython-312.pyc
    │           │   │   │   ├── kusto.cpython-312.pyc
    │           │   │   │   ├── ldap.cpython-312.pyc
    │           │   │   │   ├── lean.cpython-312.pyc
    │           │   │   │   ├── lilypond.cpython-312.pyc
    │           │   │   │   ├── lisp.cpython-312.pyc
    │           │   │   │   ├── macaulay2.cpython-312.pyc
    │           │   │   │   ├── make.cpython-312.pyc
    │           │   │   │   ├── maple.cpython-312.pyc
    │           │   │   │   ├── markup.cpython-312.pyc
    │           │   │   │   ├── math.cpython-312.pyc
    │           │   │   │   ├── matlab.cpython-312.pyc
    │           │   │   │   ├── maxima.cpython-312.pyc
    │           │   │   │   ├── meson.cpython-312.pyc
    │           │   │   │   ├── mime.cpython-312.pyc
    │           │   │   │   ├── minecraft.cpython-312.pyc
    │           │   │   │   ├── mips.cpython-312.pyc
    │           │   │   │   ├── ml.cpython-312.pyc
    │           │   │   │   ├── modeling.cpython-312.pyc
    │           │   │   │   ├── modula2.cpython-312.pyc
    │           │   │   │   ├── mojo.cpython-312.pyc
    │           │   │   │   ├── monte.cpython-312.pyc
    │           │   │   │   ├── mosel.cpython-312.pyc
    │           │   │   │   ├── ncl.cpython-312.pyc
    │           │   │   │   ├── nimrod.cpython-312.pyc
    │           │   │   │   ├── nit.cpython-312.pyc
    │           │   │   │   ├── nix.cpython-312.pyc
    │           │   │   │   ├── numbair.cpython-312.pyc
    │           │   │   │   ├── oberon.cpython-312.pyc
    │           │   │   │   ├── objective.cpython-312.pyc
    │           │   │   │   ├── ooc.cpython-312.pyc
    │           │   │   │   ├── openscad.cpython-312.pyc
    │           │   │   │   ├── other.cpython-312.pyc
    │           │   │   │   ├── parasail.cpython-312.pyc
    │           │   │   │   ├── parsers.cpython-312.pyc
    │           │   │   │   ├── pascal.cpython-312.pyc
    │           │   │   │   ├── pawn.cpython-312.pyc
    │           │   │   │   ├── pddl.cpython-312.pyc
    │           │   │   │   ├── perl.cpython-312.pyc
    │           │   │   │   ├── phix.cpython-312.pyc
    │           │   │   │   ├── php.cpython-312.pyc
    │           │   │   │   ├── pointless.cpython-312.pyc
    │           │   │   │   ├── pony.cpython-312.pyc
    │           │   │   │   ├── praat.cpython-312.pyc
    │           │   │   │   ├── procfile.cpython-312.pyc
    │           │   │   │   ├── prolog.cpython-312.pyc
    │           │   │   │   ├── promql.cpython-312.pyc
    │           │   │   │   ├── prql.cpython-312.pyc
    │           │   │   │   ├── ptx.cpython-312.pyc
    │           │   │   │   ├── python.cpython-312.pyc
    │           │   │   │   ├── q.cpython-312.pyc
    │           │   │   │   ├── qlik.cpython-312.pyc
    │           │   │   │   ├── qvt.cpython-312.pyc
    │           │   │   │   ├── r.cpython-312.pyc
    │           │   │   │   ├── rdf.cpython-312.pyc
    │           │   │   │   ├── rebol.cpython-312.pyc
    │           │   │   │   ├── rego.cpython-312.pyc
    │           │   │   │   ├── resource.cpython-312.pyc
    │           │   │   │   ├── ride.cpython-312.pyc
    │           │   │   │   ├── rita.cpython-312.pyc
    │           │   │   │   ├── rnc.cpython-312.pyc
    │           │   │   │   ├── roboconf.cpython-312.pyc
    │           │   │   │   ├── robotframework.cpython-312.pyc
    │           │   │   │   ├── ruby.cpython-312.pyc
    │           │   │   │   ├── rust.cpython-312.pyc
    │           │   │   │   ├── sas.cpython-312.pyc
    │           │   │   │   ├── savi.cpython-312.pyc
    │           │   │   │   ├── scdoc.cpython-312.pyc
    │           │   │   │   ├── scripting.cpython-312.pyc
    │           │   │   │   ├── sgf.cpython-312.pyc
    │           │   │   │   ├── shell.cpython-312.pyc
    │           │   │   │   ├── sieve.cpython-312.pyc
    │           │   │   │   ├── slash.cpython-312.pyc
    │           │   │   │   ├── smalltalk.cpython-312.pyc
    │           │   │   │   ├── smithy.cpython-312.pyc
    │           │   │   │   ├── smv.cpython-312.pyc
    │           │   │   │   ├── snobol.cpython-312.pyc
    │           │   │   │   ├── solidity.cpython-312.pyc
    │           │   │   │   ├── soong.cpython-312.pyc
    │           │   │   │   ├── sophia.cpython-312.pyc
    │           │   │   │   ├── special.cpython-312.pyc
    │           │   │   │   ├── spice.cpython-312.pyc
    │           │   │   │   ├── sql.cpython-312.pyc
    │           │   │   │   ├── srcinfo.cpython-312.pyc
    │           │   │   │   ├── stata.cpython-312.pyc
    │           │   │   │   ├── supercollider.cpython-312.pyc
    │           │   │   │   ├── tablegen.cpython-312.pyc
    │           │   │   │   ├── tact.cpython-312.pyc
    │           │   │   │   ├── tal.cpython-312.pyc
    │           │   │   │   ├── tcl.cpython-312.pyc
    │           │   │   │   ├── teal.cpython-312.pyc
    │           │   │   │   ├── templates.cpython-312.pyc
    │           │   │   │   ├── teraterm.cpython-312.pyc
    │           │   │   │   ├── testing.cpython-312.pyc
    │           │   │   │   ├── text.cpython-312.pyc
    │           │   │   │   ├── textedit.cpython-312.pyc
    │           │   │   │   ├── textfmts.cpython-312.pyc
    │           │   │   │   ├── theorem.cpython-312.pyc
    │           │   │   │   ├── thingsdb.cpython-312.pyc
    │           │   │   │   ├── tlb.cpython-312.pyc
    │           │   │   │   ├── tls.cpython-312.pyc
    │           │   │   │   ├── tnt.cpython-312.pyc
    │           │   │   │   ├── trafficscript.cpython-312.pyc
    │           │   │   │   ├── typoscript.cpython-312.pyc
    │           │   │   │   ├── typst.cpython-312.pyc
    │           │   │   │   ├── ul4.cpython-312.pyc
    │           │   │   │   ├── unicon.cpython-312.pyc
    │           │   │   │   ├── urbi.cpython-312.pyc
    │           │   │   │   ├── usd.cpython-312.pyc
    │           │   │   │   ├── varnish.cpython-312.pyc
    │           │   │   │   ├── verification.cpython-312.pyc
    │           │   │   │   ├── verifpal.cpython-312.pyc
    │           │   │   │   ├── vip.cpython-312.pyc
    │           │   │   │   ├── vyper.cpython-312.pyc
    │           │   │   │   ├── web.cpython-312.pyc
    │           │   │   │   ├── webassembly.cpython-312.pyc
    │           │   │   │   ├── webidl.cpython-312.pyc
    │           │   │   │   ├── webmisc.cpython-312.pyc
    │           │   │   │   ├── wgsl.cpython-312.pyc
    │           │   │   │   ├── whiley.cpython-312.pyc
    │           │   │   │   ├── wowtoc.cpython-312.pyc
    │           │   │   │   ├── wren.cpython-312.pyc
    │           │   │   │   ├── x10.cpython-312.pyc
    │           │   │   │   ├── xorg.cpython-312.pyc
    │           │   │   │   ├── yang.cpython-312.pyc
    │           │   │   │   ├── yara.cpython-312.pyc
    │           │   │   │   └── zig.cpython-312.pyc
    │           │   │   ├── _ada_builtins.py
    │           │   │   ├── _asy_builtins.py
    │           │   │   ├── _cl_builtins.py
    │           │   │   ├── _cocoa_builtins.py
    │           │   │   ├── _csound_builtins.py
    │           │   │   ├── _css_builtins.py
    │           │   │   ├── _googlesql_builtins.py
    │           │   │   ├── _julia_builtins.py
    │           │   │   ├── _lasso_builtins.py
    │           │   │   ├── _lilypond_builtins.py
    │           │   │   ├── _lua_builtins.py
    │           │   │   ├── _luau_builtins.py
    │           │   │   ├── _mapping.py
    │           │   │   ├── _mql_builtins.py
    │           │   │   ├── _mysql_builtins.py
    │           │   │   ├── _openedge_builtins.py
    │           │   │   ├── _php_builtins.py
    │           │   │   ├── _postgres_builtins.py
    │           │   │   ├── _qlik_builtins.py
    │           │   │   ├── _scheme_builtins.py
    │           │   │   ├── _scilab_builtins.py
    │           │   │   ├── _sourcemod_builtins.py
    │           │   │   ├── _sql_builtins.py
    │           │   │   ├── _stan_builtins.py
    │           │   │   ├── _stata_builtins.py
    │           │   │   ├── _tsql_builtins.py
    │           │   │   ├── _usd_builtins.py
    │           │   │   ├── _vbscript_builtins.py
    │           │   │   ├── _vim_builtins.py
    │           │   │   ├── actionscript.py
    │           │   │   ├── ada.py
    │           │   │   ├── agile.py
    │           │   │   ├── algebra.py
    │           │   │   ├── ambient.py
    │           │   │   ├── amdgpu.py
    │           │   │   ├── ampl.py
    │           │   │   ├── apdlexer.py
    │           │   │   ├── apl.py
    │           │   │   ├── archetype.py
    │           │   │   ├── arrow.py
    │           │   │   ├── arturo.py
    │           │   │   ├── asc.py
    │           │   │   ├── asm.py
    │           │   │   ├── asn1.py
    │           │   │   ├── automation.py
    │           │   │   ├── bare.py
    │           │   │   ├── basic.py
    │           │   │   ├── bdd.py
    │           │   │   ├── berry.py
    │           │   │   ├── bibtex.py
    │           │   │   ├── blueprint.py
    │           │   │   ├── boa.py
    │           │   │   ├── bqn.py
    │           │   │   ├── business.py
    │           │   │   ├── c_cpp.py
    │           │   │   ├── c_like.py
    │           │   │   ├── capnproto.py
    │           │   │   ├── carbon.py
    │           │   │   ├── cddl.py
    │           │   │   ├── chapel.py
    │           │   │   ├── clean.py
    │           │   │   ├── codeql.py
    │           │   │   ├── comal.py
    │           │   │   ├── compiled.py
    │           │   │   ├── configs.py
    │           │   │   ├── console.py
    │           │   │   ├── cplint.py
    │           │   │   ├── crystal.py
    │           │   │   ├── csound.py
    │           │   │   ├── css.py
    │           │   │   ├── d.py
    │           │   │   ├── dalvik.py
    │           │   │   ├── data.py
    │           │   │   ├── dax.py
    │           │   │   ├── devicetree.py
    │           │   │   ├── diff.py
    │           │   │   ├── dns.py
    │           │   │   ├── dotnet.py
    │           │   │   ├── dsls.py
    │           │   │   ├── dylan.py
    │           │   │   ├── ecl.py
    │           │   │   ├── eiffel.py
    │           │   │   ├── elm.py
    │           │   │   ├── elpi.py
    │           │   │   ├── email.py
    │           │   │   ├── erlang.py
    │           │   │   ├── esoteric.py
    │           │   │   ├── ezhil.py
    │           │   │   ├── factor.py
    │           │   │   ├── fantom.py
    │           │   │   ├── felix.py
    │           │   │   ├── fift.py
    │           │   │   ├── floscript.py
    │           │   │   ├── forth.py
    │           │   │   ├── fortran.py
    │           │   │   ├── foxpro.py
    │           │   │   ├── freefem.py
    │           │   │   ├── func.py
    │           │   │   ├── functional.py
    │           │   │   ├── futhark.py
    │           │   │   ├── gcodelexer.py
    │           │   │   ├── gdscript.py
    │           │   │   ├── gleam.py
    │           │   │   ├── go.py
    │           │   │   ├── grammar_notation.py
    │           │   │   ├── graph.py
    │           │   │   ├── graphics.py
    │           │   │   ├── graphql.py
    │           │   │   ├── graphviz.py
    │           │   │   ├── gsql.py
    │           │   │   ├── hare.py
    │           │   │   ├── haskell.py
    │           │   │   ├── haxe.py
    │           │   │   ├── hdl.py
    │           │   │   ├── hexdump.py
    │           │   │   ├── html.py
    │           │   │   ├── idl.py
    │           │   │   ├── igor.py
    │           │   │   ├── inferno.py
    │           │   │   ├── installers.py
    │           │   │   ├── int_fiction.py
    │           │   │   ├── iolang.py
    │           │   │   ├── j.py
    │           │   │   ├── javascript.py
    │           │   │   ├── jmespath.py
    │           │   │   ├── jslt.py
    │           │   │   ├── json5.py
    │           │   │   ├── jsonnet.py
    │           │   │   ├── jsx.py
    │           │   │   ├── julia.py
    │           │   │   ├── jvm.py
    │           │   │   ├── kuin.py
    │           │   │   ├── kusto.py
    │           │   │   ├── ldap.py
    │           │   │   ├── lean.py
    │           │   │   ├── lilypond.py
    │           │   │   ├── lisp.py
    │           │   │   ├── macaulay2.py
    │           │   │   ├── make.py
    │           │   │   ├── maple.py
    │           │   │   ├── markup.py
    │           │   │   ├── math.py
    │           │   │   ├── matlab.py
    │           │   │   ├── maxima.py
    │           │   │   ├── meson.py
    │           │   │   ├── mime.py
    │           │   │   ├── minecraft.py
    │           │   │   ├── mips.py
    │           │   │   ├── ml.py
    │           │   │   ├── modeling.py
    │           │   │   ├── modula2.py
    │           │   │   ├── mojo.py
    │           │   │   ├── monte.py
    │           │   │   ├── mosel.py
    │           │   │   ├── ncl.py
    │           │   │   ├── nimrod.py
    │           │   │   ├── nit.py
    │           │   │   ├── nix.py
    │           │   │   ├── numbair.py
    │           │   │   ├── oberon.py
    │           │   │   ├── objective.py
    │           │   │   ├── ooc.py
    │           │   │   ├── openscad.py
    │           │   │   ├── other.py
    │           │   │   ├── parasail.py
    │           │   │   ├── parsers.py
    │           │   │   ├── pascal.py
    │           │   │   ├── pawn.py
    │           │   │   ├── pddl.py
    │           │   │   ├── perl.py
    │           │   │   ├── phix.py
    │           │   │   ├── php.py
    │           │   │   ├── pointless.py
    │           │   │   ├── pony.py
    │           │   │   ├── praat.py
    │           │   │   ├── procfile.py
    │           │   │   ├── prolog.py
    │           │   │   ├── promql.py
    │           │   │   ├── prql.py
    │           │   │   ├── ptx.py
    │           │   │   ├── python.py
    │           │   │   ├── q.py
    │           │   │   ├── qlik.py
    │           │   │   ├── qvt.py
    │           │   │   ├── r.py
    │           │   │   ├── rdf.py
    │           │   │   ├── rebol.py
    │           │   │   ├── rego.py
    │           │   │   ├── resource.py
    │           │   │   ├── ride.py
    │           │   │   ├── rita.py
    │           │   │   ├── rnc.py
    │           │   │   ├── roboconf.py
    │           │   │   ├── robotframework.py
    │           │   │   ├── ruby.py
    │           │   │   ├── rust.py
    │           │   │   ├── sas.py
    │           │   │   ├── savi.py
    │           │   │   ├── scdoc.py
    │           │   │   ├── scripting.py
    │           │   │   ├── sgf.py
    │           │   │   ├── shell.py
    │           │   │   ├── sieve.py
    │           │   │   ├── slash.py
    │           │   │   ├── smalltalk.py
    │           │   │   ├── smithy.py
    │           │   │   ├── smv.py
    │           │   │   ├── snobol.py
    │           │   │   ├── solidity.py
    │           │   │   ├── soong.py
    │           │   │   ├── sophia.py
    │           │   │   ├── special.py
    │           │   │   ├── spice.py
    │           │   │   ├── sql.py
    │           │   │   ├── srcinfo.py
    │           │   │   ├── stata.py
    │           │   │   ├── supercollider.py
    │           │   │   ├── tablegen.py
    │           │   │   ├── tact.py
    │           │   │   ├── tal.py
    │           │   │   ├── tcl.py
    │           │   │   ├── teal.py
    │           │   │   ├── templates.py
    │           │   │   ├── teraterm.py
    │           │   │   ├── testing.py
    │           │   │   ├── text.py
    │           │   │   ├── textedit.py
    │           │   │   ├── textfmts.py
    │           │   │   ├── theorem.py
    │           │   │   ├── thingsdb.py
    │           │   │   ├── tlb.py
    │           │   │   ├── tls.py
    │           │   │   ├── tnt.py
    │           │   │   ├── trafficscript.py
    │           │   │   ├── typoscript.py
    │           │   │   ├── typst.py
    │           │   │   ├── ul4.py
    │           │   │   ├── unicon.py
    │           │   │   ├── urbi.py
    │           │   │   ├── usd.py
    │           │   │   ├── varnish.py
    │           │   │   ├── verification.py
    │           │   │   ├── verifpal.py
    │           │   │   ├── vip.py
    │           │   │   ├── vyper.py
    │           │   │   ├── web.py
    │           │   │   ├── webassembly.py
    │           │   │   ├── webidl.py
    │           │   │   ├── webmisc.py
    │           │   │   ├── wgsl.py
    │           │   │   ├── whiley.py
    │           │   │   ├── wowtoc.py
    │           │   │   ├── wren.py
    │           │   │   ├── x10.py
    │           │   │   ├── xorg.py
    │           │   │   ├── yang.py
    │           │   │   ├── yara.py
    │           │   │   └── zig.py
    │           │   ├── modeline.py
    │           │   ├── plugin.py
    │           │   ├── regexopt.py
    │           │   ├── scanner.py
    │           │   ├── sphinxext.py
    │           │   ├── style.py
    │           │   ├── [01;34mstyles[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── _mapping.cpython-312.pyc
    │           │   │   │   ├── abap.cpython-312.pyc
    │           │   │   │   ├── algol.cpython-312.pyc
    │           │   │   │   ├── algol_nu.cpython-312.pyc
    │           │   │   │   ├── arduino.cpython-312.pyc
    │           │   │   │   ├── autumn.cpython-312.pyc
    │           │   │   │   ├── borland.cpython-312.pyc
    │           │   │   │   ├── bw.cpython-312.pyc
    │           │   │   │   ├── coffee.cpython-312.pyc
    │           │   │   │   ├── colorful.cpython-312.pyc
    │           │   │   │   ├── default.cpython-312.pyc
    │           │   │   │   ├── dracula.cpython-312.pyc
    │           │   │   │   ├── emacs.cpython-312.pyc
    │           │   │   │   ├── friendly.cpython-312.pyc
    │           │   │   │   ├── friendly_grayscale.cpython-312.pyc
    │           │   │   │   ├── fruity.cpython-312.pyc
    │           │   │   │   ├── gh_dark.cpython-312.pyc
    │           │   │   │   ├── gruvbox.cpython-312.pyc
    │           │   │   │   ├── igor.cpython-312.pyc
    │           │   │   │   ├── inkpot.cpython-312.pyc
    │           │   │   │   ├── lightbulb.cpython-312.pyc
    │           │   │   │   ├── lilypond.cpython-312.pyc
    │           │   │   │   ├── lovelace.cpython-312.pyc
    │           │   │   │   ├── manni.cpython-312.pyc
    │           │   │   │   ├── material.cpython-312.pyc
    │           │   │   │   ├── monokai.cpython-312.pyc
    │           │   │   │   ├── murphy.cpython-312.pyc
    │           │   │   │   ├── native.cpython-312.pyc
    │           │   │   │   ├── nord.cpython-312.pyc
    │           │   │   │   ├── onedark.cpython-312.pyc
    │           │   │   │   ├── paraiso_dark.cpython-312.pyc
    │           │   │   │   ├── paraiso_light.cpython-312.pyc
    │           │   │   │   ├── pastie.cpython-312.pyc
    │           │   │   │   ├── perldoc.cpython-312.pyc
    │           │   │   │   ├── rainbow_dash.cpython-312.pyc
    │           │   │   │   ├── rrt.cpython-312.pyc
    │           │   │   │   ├── sas.cpython-312.pyc
    │           │   │   │   ├── solarized.cpython-312.pyc
    │           │   │   │   ├── staroffice.cpython-312.pyc
    │           │   │   │   ├── stata_dark.cpython-312.pyc
    │           │   │   │   ├── stata_light.cpython-312.pyc
    │           │   │   │   ├── tango.cpython-312.pyc
    │           │   │   │   ├── trac.cpython-312.pyc
    │           │   │   │   ├── vim.cpython-312.pyc
    │           │   │   │   ├── vs.cpython-312.pyc
    │           │   │   │   ├── xcode.cpython-312.pyc
    │           │   │   │   └── zenburn.cpython-312.pyc
    │           │   │   ├── _mapping.py
    │           │   │   ├── abap.py
    │           │   │   ├── algol.py
    │           │   │   ├── algol_nu.py
    │           │   │   ├── arduino.py
    │           │   │   ├── autumn.py
    │           │   │   ├── borland.py
    │           │   │   ├── bw.py
    │           │   │   ├── coffee.py
    │           │   │   ├── colorful.py
    │           │   │   ├── default.py
    │           │   │   ├── dracula.py
    │           │   │   ├── emacs.py
    │           │   │   ├── friendly.py
    │           │   │   ├── friendly_grayscale.py
    │           │   │   ├── fruity.py
    │           │   │   ├── gh_dark.py
    │           │   │   ├── gruvbox.py
    │           │   │   ├── igor.py
    │           │   │   ├── inkpot.py
    │           │   │   ├── lightbulb.py
    │           │   │   ├── lilypond.py
    │           │   │   ├── lovelace.py
    │           │   │   ├── manni.py
    │           │   │   ├── material.py
    │           │   │   ├── monokai.py
    │           │   │   ├── murphy.py
    │           │   │   ├── native.py
    │           │   │   ├── nord.py
    │           │   │   ├── onedark.py
    │           │   │   ├── paraiso_dark.py
    │           │   │   ├── paraiso_light.py
    │           │   │   ├── pastie.py
    │           │   │   ├── perldoc.py
    │           │   │   ├── rainbow_dash.py
    │           │   │   ├── rrt.py
    │           │   │   ├── sas.py
    │           │   │   ├── solarized.py
    │           │   │   ├── staroffice.py
    │           │   │   ├── stata_dark.py
    │           │   │   ├── stata_light.py
    │           │   │   ├── tango.py
    │           │   │   ├── trac.py
    │           │   │   ├── vim.py
    │           │   │   ├── vs.py
    │           │   │   ├── xcode.py
    │           │   │   └── zenburn.py
    │           │   ├── token.py
    │           │   ├── unistring.py
    │           │   └── util.py
    │           ├── [01;34mpygments-2.19.2.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   └── [01;34mlicenses[0m
    │           │       ├── AUTHORS
    │           │       └── LICENSE
    │           ├── [01;34mpytest[0m
    │           │   ├── __init__.py
    │           │   ├── __main__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   └── __main__.cpython-312.pyc
    │           │   └── py.typed
    │           ├── [01;34mpytest-9.0.2.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── REQUESTED
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   ├── [01;34mlicenses[0m
    │           │   │   └── LICENSE
    │           │   └── top_level.txt
    │           ├── [01;34mpython_dotenv-1.2.2.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── REQUESTED
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   ├── [01;34mlicenses[0m
    │           │   │   └── LICENSE
    │           │   └── top_level.txt
    │           ├── [01;34mpython_multipart[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── decoders.cpython-312.pyc
    │           │   │   ├── exceptions.cpython-312.pyc
    │           │   │   └── multipart.cpython-312.pyc
    │           │   ├── decoders.py
    │           │   ├── exceptions.py
    │           │   ├── multipart.py
    │           │   └── py.typed
    │           ├── [01;34mpython_multipart-0.0.22.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── REQUESTED
    │           │   ├── WHEEL
    │           │   └── [01;34mlicenses[0m
    │           │       └── LICENSE.txt
    │           ├── [01;34mstarlette[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── _exception_handler.cpython-312.pyc
    │           │   │   ├── _utils.cpython-312.pyc
    │           │   │   ├── applications.cpython-312.pyc
    │           │   │   ├── authentication.cpython-312.pyc
    │           │   │   ├── background.cpython-312.pyc
    │           │   │   ├── concurrency.cpython-312.pyc
    │           │   │   ├── config.cpython-312.pyc
    │           │   │   ├── convertors.cpython-312.pyc
    │           │   │   ├── datastructures.cpython-312.pyc
    │           │   │   ├── endpoints.cpython-312.pyc
    │           │   │   ├── exceptions.cpython-312.pyc
    │           │   │   ├── formparsers.cpython-312.pyc
    │           │   │   ├── requests.cpython-312.pyc
    │           │   │   ├── responses.cpython-312.pyc
    │           │   │   ├── routing.cpython-312.pyc
    │           │   │   ├── schemas.cpython-312.pyc
    │           │   │   ├── staticfiles.cpython-312.pyc
    │           │   │   ├── status.cpython-312.pyc
    │           │   │   ├── templating.cpython-312.pyc
    │           │   │   ├── testclient.cpython-312.pyc
    │           │   │   ├── types.cpython-312.pyc
    │           │   │   └── websockets.cpython-312.pyc
    │           │   ├── _exception_handler.py
    │           │   ├── _utils.py
    │           │   ├── applications.py
    │           │   ├── authentication.py
    │           │   ├── background.py
    │           │   ├── concurrency.py
    │           │   ├── config.py
    │           │   ├── convertors.py
    │           │   ├── datastructures.py
    │           │   ├── endpoints.py
    │           │   ├── exceptions.py
    │           │   ├── formparsers.py
    │           │   ├── [01;34mmiddleware[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── authentication.cpython-312.pyc
    │           │   │   │   ├── base.cpython-312.pyc
    │           │   │   │   ├── cors.cpython-312.pyc
    │           │   │   │   ├── errors.cpython-312.pyc
    │           │   │   │   ├── exceptions.cpython-312.pyc
    │           │   │   │   ├── gzip.cpython-312.pyc
    │           │   │   │   ├── httpsredirect.cpython-312.pyc
    │           │   │   │   ├── sessions.cpython-312.pyc
    │           │   │   │   ├── trustedhost.cpython-312.pyc
    │           │   │   │   └── wsgi.cpython-312.pyc
    │           │   │   ├── authentication.py
    │           │   │   ├── base.py
    │           │   │   ├── cors.py
    │           │   │   ├── errors.py
    │           │   │   ├── exceptions.py
    │           │   │   ├── gzip.py
    │           │   │   ├── httpsredirect.py
    │           │   │   ├── sessions.py
    │           │   │   ├── trustedhost.py
    │           │   │   └── wsgi.py
    │           │   ├── py.typed
    │           │   ├── requests.py
    │           │   ├── responses.py
    │           │   ├── routing.py
    │           │   ├── schemas.py
    │           │   ├── staticfiles.py
    │           │   ├── status.py
    │           │   ├── templating.py
    │           │   ├── testclient.py
    │           │   ├── types.py
    │           │   └── websockets.py
    │           ├── [01;34mstarlette-0.52.1.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── [01;34mlicenses[0m
    │           │       └── LICENSE.md
    │           ├── [01;34mtyping_extensions-4.15.0.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── [01;34mlicenses[0m
    │           │       └── LICENSE
    │           ├── typing_extensions.py
    │           ├── [01;34mtyping_inspection[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── introspection.cpython-312.pyc
    │           │   │   └── typing_objects.cpython-312.pyc
    │           │   ├── introspection.py
    │           │   ├── py.typed
    │           │   ├── typing_objects.py
    │           │   └── typing_objects.pyi
    │           ├── [01;34mtyping_inspection-0.4.2.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── WHEEL
    │           │   └── [01;34mlicenses[0m
    │           │       └── LICENSE
    │           ├── [01;34muvicorn[0m
    │           │   ├── __init__.py
    │           │   ├── __main__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── __main__.cpython-312.pyc
    │           │   │   ├── _compat.cpython-312.pyc
    │           │   │   ├── _subprocess.cpython-312.pyc
    │           │   │   ├── _types.cpython-312.pyc
    │           │   │   ├── config.cpython-312.pyc
    │           │   │   ├── importer.cpython-312.pyc
    │           │   │   ├── logging.cpython-312.pyc
    │           │   │   ├── main.cpython-312.pyc
    │           │   │   ├── server.cpython-312.pyc
    │           │   │   └── workers.cpython-312.pyc
    │           │   ├── _compat.py
    │           │   ├── _subprocess.py
    │           │   ├── _types.py
    │           │   ├── config.py
    │           │   ├── importer.py
    │           │   ├── [01;34mlifespan[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── off.cpython-312.pyc
    │           │   │   │   └── on.cpython-312.pyc
    │           │   │   ├── off.py
    │           │   │   └── on.py
    │           │   ├── logging.py
    │           │   ├── [01;34mloops[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── asyncio.cpython-312.pyc
    │           │   │   │   ├── auto.cpython-312.pyc
    │           │   │   │   └── uvloop.cpython-312.pyc
    │           │   │   ├── asyncio.py
    │           │   │   ├── auto.py
    │           │   │   └── uvloop.py
    │           │   ├── main.py
    │           │   ├── [01;34mmiddleware[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── asgi2.cpython-312.pyc
    │           │   │   │   ├── message_logger.cpython-312.pyc
    │           │   │   │   ├── proxy_headers.cpython-312.pyc
    │           │   │   │   └── wsgi.cpython-312.pyc
    │           │   │   ├── asgi2.py
    │           │   │   ├── message_logger.py
    │           │   │   ├── proxy_headers.py
    │           │   │   └── wsgi.py
    │           │   ├── [01;34mprotocols[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   └── utils.cpython-312.pyc
    │           │   │   ├── [01;34mhttp[0m
    │           │   │   │   ├── __init__.py
    │           │   │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   │   ├── auto.cpython-312.pyc
    │           │   │   │   │   ├── flow_control.cpython-312.pyc
    │           │   │   │   │   ├── h11_impl.cpython-312.pyc
    │           │   │   │   │   └── httptools_impl.cpython-312.pyc
    │           │   │   │   ├── auto.py
    │           │   │   │   ├── flow_control.py
    │           │   │   │   ├── h11_impl.py
    │           │   │   │   └── httptools_impl.py
    │           │   │   ├── utils.py
    │           │   │   └── [01;34mwebsockets[0m
    │           │   │       ├── __init__.py
    │           │   │       ├── [01;34m__pycache__[0m
    │           │   │       │   ├── __init__.cpython-312.pyc
    │           │   │       │   ├── auto.cpython-312.pyc
    │           │   │       │   ├── websockets_impl.cpython-312.pyc
    │           │   │       │   ├── websockets_sansio_impl.cpython-312.pyc
    │           │   │       │   └── wsproto_impl.cpython-312.pyc
    │           │   │       ├── auto.py
    │           │   │       ├── websockets_impl.py
    │           │   │       ├── websockets_sansio_impl.py
    │           │   │       └── wsproto_impl.py
    │           │   ├── py.typed
    │           │   ├── server.py
    │           │   ├── [01;34msupervisors[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── basereload.cpython-312.pyc
    │           │   │   │   ├── multiprocess.cpython-312.pyc
    │           │   │   │   ├── statreload.cpython-312.pyc
    │           │   │   │   └── watchfilesreload.cpython-312.pyc
    │           │   │   ├── basereload.py
    │           │   │   ├── multiprocess.py
    │           │   │   ├── statreload.py
    │           │   │   └── watchfilesreload.py
    │           │   └── workers.py
    │           ├── [01;34muvicorn-0.41.0.dist-info[0m
    │           │   ├── INSTALLER
    │           │   ├── METADATA
    │           │   ├── RECORD
    │           │   ├── REQUESTED
    │           │   ├── WHEEL
    │           │   ├── entry_points.txt
    │           │   └── [01;34mlicenses[0m
    │           │       └── LICENSE.md
    │           ├── [01;34mxmlschema[0m
    │           │   ├── __init__.py
    │           │   ├── [01;34m__pycache__[0m
    │           │   │   ├── __init__.cpython-312.pyc
    │           │   │   ├── aliases.cpython-312.pyc
    │           │   │   ├── cli.cpython-312.pyc
    │           │   │   ├── dataobjects.cpython-312.pyc
    │           │   │   ├── documents.cpython-312.pyc
    │           │   │   ├── exceptions.cpython-312.pyc
    │           │   │   ├── exports.cpython-312.pyc
    │           │   │   ├── helpers.cpython-312.pyc
    │           │   │   ├── limits.cpython-312.pyc
    │           │   │   ├── locations.cpython-312.pyc
    │           │   │   ├── names.cpython-312.pyc
    │           │   │   ├── namespaces.cpython-312.pyc
    │           │   │   ├── resources.cpython-312.pyc
    │           │   │   ├── translation.cpython-312.pyc
    │           │   │   └── xpath3.cpython-312.pyc
    │           │   ├── aliases.py
    │           │   ├── cli.py
    │           │   ├── [01;34mconverters[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── abdera.cpython-312.pyc
    │           │   │   │   ├── badgerfish.cpython-312.pyc
    │           │   │   │   ├── columnar.cpython-312.pyc
    │           │   │   │   ├── default.cpython-312.pyc
    │           │   │   │   ├── gdata.cpython-312.pyc
    │           │   │   │   ├── jsonml.cpython-312.pyc
    │           │   │   │   ├── parker.cpython-312.pyc
    │           │   │   │   └── unordered.cpython-312.pyc
    │           │   │   ├── abdera.py
    │           │   │   ├── badgerfish.py
    │           │   │   ├── columnar.py
    │           │   │   ├── default.py
    │           │   │   ├── gdata.py
    │           │   │   ├── jsonml.py
    │           │   │   ├── parker.py
    │           │   │   └── unordered.py
    │           │   ├── dataobjects.py
    │           │   ├── documents.py
    │           │   ├── exceptions.py
    │           │   ├── exports.py
    │           │   ├── [01;34mextras[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── codegen.cpython-312.pyc
    │           │   │   │   └── wsdl.cpython-312.pyc
    │           │   │   ├── codegen.py
    │           │   │   ├── [01;34mtemplates[0m
    │           │   │   │   └── [01;34mpython[0m
    │           │   │   │       ├── bindings.py.jinja
    │           │   │   │       └── sample.py.jinja
    │           │   │   └── wsdl.py
    │           │   ├── helpers.py
    │           │   ├── limits.py
    │           │   ├── [01;34mlocale[0m
    │           │   │   ├── [01;34men[0m
    │           │   │   │   └── [01;34mLC_MESSAGES[0m
    │           │   │   │       ├── xmlschema.mo
    │           │   │   │       └── xmlschema.po
    │           │   │   ├── [01;34mit[0m
    │           │   │   │   └── [01;34mLC_MESSAGES[0m
    │           │   │   │       ├── xmlschema.mo
    │           │   │   │       └── xmlschema.po
    │           │   │   ├── [01;34mpl[0m
    │           │   │   │   └── [01;34mLC_MESSAGES[0m
    │           │   │   │       ├── xmlschema.mo
    │           │   │   │       └── xmlschema.po
    │           │   │   └── [01;34mru[0m
    │           │   │       └── [01;34mLC_MESSAGES[0m
    │           │   │           ├── xmlschema.mo
    │           │   │           └── xmlschema.po
    │           │   ├── locations.py
    │           │   ├── names.py
    │           │   ├── namespaces.py
    │           │   ├── py.typed
    │           │   ├── resources.py
    │           │   ├── [01;34mschemas[0m
    │           │   │   ├── [01;34mDSIG[0m
    │           │   │   │   ├── xmldsig-core-schema.xsd
    │           │   │   │   └── xmldsig11-schema.xsd
    │           │   │   ├── [01;34mHFP[0m
    │           │   │   │   └── XMLSchema-hasFacetAndProperty_minimal.xsd
    │           │   │   ├── [01;34mVC[0m
    │           │   │   │   └── XMLSchema-versioning.xsd
    │           │   │   ├── [01;34mWSDL[0m
    │           │   │   │   ├── soap-encoding.xsd
    │           │   │   │   ├── soap-envelope.xsd
    │           │   │   │   ├── wsdl-soap.xsd
    │           │   │   │   └── wsdl.xsd
    │           │   │   ├── [01;34mXENC[0m
    │           │   │   │   ├── xenc-schema-11.xsd
    │           │   │   │   └── xenc-schema.xsd
    │           │   │   ├── [01;34mXHTML[0m
    │           │   │   │   └── xhtml1-strict.xsd
    │           │   │   ├── [01;34mXLINK[0m
    │           │   │   │   └── xlink.xsd
    │           │   │   ├── [01;34mXML[0m
    │           │   │   │   └── xml_minimal.xsd
    │           │   │   ├── [01;34mXSD_1.0[0m
    │           │   │   │   ├── XMLSchema.xsd
    │           │   │   │   └── datatypes.xsd
    │           │   │   ├── [01;34mXSD_1.1[0m
    │           │   │   │   ├── XMLSchema.xsd
    │           │   │   │   ├── datatypes.xsd
    │           │   │   │   └── xsd11-extra.xsd
    │           │   │   └── [01;34mXSI[0m
    │           │   │       └── XMLSchema-instance_minimal.xsd
    │           │   ├── [01;34mtesting[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── _builders.cpython-312.pyc
    │           │   │   │   ├── _case_class.cpython-312.pyc
    │           │   │   │   ├── _factory.cpython-312.pyc
    │           │   │   │   ├── _helpers.cpython-312.pyc
    │           │   │   │   └── _observers.cpython-312.pyc
    │           │   │   ├── _builders.py
    │           │   │   ├── _case_class.py
    │           │   │   ├── _factory.py
    │           │   │   ├── _helpers.py
    │           │   │   └── _observers.py
    │           │   ├── translation.py
    │           │   ├── [01;34mvalidators[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── assertions.cpython-312.pyc
    │           │   │   │   ├── attributes.cpython-312.pyc
    │           │   │   │   ├── builtins.cpython-312.pyc
    │           │   │   │   ├── complex_types.cpython-312.pyc
    │           │   │   │   ├── elements.cpython-312.pyc
    │           │   │   │   ├── exceptions.cpython-312.pyc
    │           │   │   │   ├── facets.cpython-312.pyc
    │           │   │   │   ├── global_maps.cpython-312.pyc
    │           │   │   │   ├── groups.cpython-312.pyc
    │           │   │   │   ├── helpers.cpython-312.pyc
    │           │   │   │   ├── identities.cpython-312.pyc
    │           │   │   │   ├── models.cpython-312.pyc
    │           │   │   │   ├── notations.cpython-312.pyc
    │           │   │   │   ├── particles.cpython-312.pyc
    │           │   │   │   ├── schemas.cpython-312.pyc
    │           │   │   │   ├── simple_types.cpython-312.pyc
    │           │   │   │   ├── wildcards.cpython-312.pyc
    │           │   │   │   └── xsdbase.cpython-312.pyc
    │           │   │   ├── assertions.py
    │           │   │   ├── attributes.py
    │           │   │   ├── builtins.py
    │           │   │   ├── complex_types.py
    │           │   │   ├── elements.py
    │           │   │   ├── exceptions.py
    │           │   │   ├── facets.py
    │           │   │   ├── global_maps.py
    │           │   │   ├── groups.py
    │           │   │   ├── helpers.py
    │           │   │   ├── identities.py
    │           │   │   ├── models.py
    │           │   │   ├── notations.py
    │           │   │   ├── particles.py
    │           │   │   ├── schemas.py
    │           │   │   ├── simple_types.py
    │           │   │   ├── wildcards.py
    │           │   │   └── xsdbase.py
    │           │   ├── [01;34mxpath[0m
    │           │   │   ├── __init__.py
    │           │   │   ├── [01;34m__pycache__[0m
    │           │   │   │   ├── __init__.cpython-312.pyc
    │           │   │   │   ├── assertion_parser.cpython-312.pyc
    │           │   │   │   ├── identity_parser.cpython-312.pyc
    │           │   │   │   ├── mixin.cpython-312.pyc
    │           │   │   │   └── proxy.cpython-312.pyc
    │           │   │   ├── assertion_parser.py
    │           │   │   ├── identity_parser.py
    │           │   │   ├── mixin.py
    │           │   │   └── proxy.py
    │           │   └── xpath3.py
    │           └── [01;34mxmlschema-3.4.2.dist-info[0m
    │               ├── INSTALLER
    │               ├── LICENSE
    │               ├── METADATA
    │               ├── RECORD
    │               ├── REQUESTED
    │               ├── WHEEL
    │               ├── entry_points.txt
    │               └── top_level.txt
    ├── [01;36mlib64[0m -> [01;34mlib[0m
    └── pyvenv.cfg

693 directories, 6364 files
