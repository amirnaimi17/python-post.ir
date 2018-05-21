def make_envelope(**kwargs):
    return """    <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
        <s:Body>
            <PushVarContractParcels xmlns="http://tempuri.org/">
                <VarContractDT>
                    <xs:schema id="NewDataSet" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns=""
                               xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
                        <xs:element name="NewDataSet" msdata:IsDataSet="true" msdata:UseCurrentLocale="true">
                            <xs:complexType>
                                <xs:choice minOccurs="0" maxOccurs="unbounded">
                                    <xs:element name="data_table">
                                        <xs:complexType>
                                            <xs:sequence>
                                                <xs:element name="contract_code" type="xs:int" minOccurs="1"/>
                                                <xs:element name="barcode" type="xs:string" minOccurs="1"/>
                                                <xs:element name="service_type" type="xs:int" minOccurs="0"/>
                                                <xs:element name="parcel_type" type="xs:unsignedByte" minOccurs="1"/>
                                                <xs:element name="source_tracking_code" type="xs:int" minOccurs="1"/>
                                                <xs:element name="destination_city_code" type="xs:int" minOccurs="1"/>
                                                <xs:element name="sender_name" type="xs:string" minOccurs="0"/>
                                                <xs:element name="receiver_name" type="xs:string" minOccurs="0"/>
                                                <xs:element name="parcel_accept_date" type="xs:string" minOccurs="1"/>
                                                <xs:element name="parcel_accept_time" type="xs:string" minOccurs="0"/>
                                                <xs:element name="receiver_postal_code" type="xs:string" minOccurs="0"/>
                                                <xs:element name="sender_postal_code" type="xs:string" minOccurs="0"/>
                                                <xs:element name="post_cost" type="xs:string" minOccurs="1"/>
                                                <xs:element name="company_cost" type="xs:string" minOccurs="1"/>
                                                <xs:element name="total_cost" type="xs:string" minOccurs="1"/>
                                                <xs:element name="VAT" type="xs:string" minOccurs="1"/>
                                                <xs:element name="weight" type="xs:int" minOccurs="1"/>
                                                <xs:element name="main_container_type" type="xs:short" minOccurs="0"/>
                                                <xs:element name="sub_container_type"
                                                            msdata:DataType="System.Char[], mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
                                                            type="xs:anyType" minOccurs="0"/>
                                                <xs:element name="insurance_cost" type="xs:int" minOccurs="0"/>
                                                <xs:element name="other_info" type="xs:string" minOccurs="0"/>
                                                <xs:element name="sender_national_number" type="xs:string" minOccurs="0"/>
                                                <xs:element name="receiver_national_number" type="xs:string" minOccurs="0"/>
                                            </xs:sequence>
                                        </xs:complexType>
                                    </xs:element>
                                </xs:choice>
                            </xs:complexType>
                        </xs:element>
                    </xs:schema>
                    <diffgr:diffgram xmlns:diffgr="urn:schemas-microsoft-com:xml-diffgram-v1"
                                     xmlns:msdata="urn:schemas-microsoft-com:xml-msdata">
                        <NewDataSet xmlns="">
                            <data_table diffgr:id="data_table1" msdata:rowOrder="0" diffgr:hasChanges="inserted">
                                <contract_code>{contract_code}</contract_code>
                                <barcode>{barcode}</barcode>
                                <service_type>{service_type}</service_type>
                                <parcel_type>{parcel_type}</parcel_type>
                                <source_tracking_code>{source_tracking_code}</source_tracking_code>
                                <destination_city_code>{destination_city_code}</destination_city_code>
                                <sender_name>{sender_name}</sender_name>
                                <receiver_name>{receiver_name}</receiver_name>
                                <parcel_accept_date>{parcel_accept_date}</parcel_accept_date>
                                <parcel_accept_time>{parcel_accept_time}</parcel_accept_time>
                                <receiver_postal_code>{receiver_postal_code}</receiver_postal_code>
                                <sender_postal_code>{sender_postal_code}</sender_postal_code>
                                <post_cost>{post_cost}</post_cost>
                                <company_cost>{company_cost}</company_cost>
                                <total_cost>{total_cost}</total_cost>
                                <VAT>{VAT}</VAT>
                                <weight>{weight}</weight>
                                <main_container_type>{main_container_type}</main_container_type>
                                <sub_container_type>
                                    <char>{sub_container_type}</char>
                                </sub_container_type>
                                <insurance_cost>{insurance_cost}</insurance_cost>
                            </data_table>
                        </NewDataSet>
                    </diffgr:diffgram>
                </VarContractDT>
                <ContractCode>1013034</ContractCode>
                <Password>R@stak_Pan@h%m13</Password>
            </PushVarContractParcels>
        </s:Body>
    </s:Envelope>  """.format(contract_code=kwargs.get('contract_code'), barcode=kwargs.get('barcode'),
                              service_type=kwargs.get('service_type'),
                              parcel_type=kwargs.get('parcel_type'),
                              source_tracking_code=kwargs.get('source_tracking_code'),
                              destination_city_code=kwargs.get('destination_city_code'),
                              sender_name=kwargs.get('sender_name'),
                              receiver_name=kwargs.get('receiver_name'),
                              parcel_accept_date=kwargs.get('parcel_accept_date'),
                              parcel_accept_time=kwargs.get('parcel_accept_time'),
                              receiver_postal_code=kwargs.get('receiver_postal_code'),
                              sender_postal_code=kwargs.get('sender_postal_code'), post_cost=kwargs.get('post_cost'),
                              company_cost=kwargs.get('company_cost'), total_cost=kwargs.get('total_cost'),
                              VAT=kwargs.get('VAT'),
                              weight=kwargs.get('weight'), main_container_type=kwargs.get('main_container_type'),
                              sub_container_type=kwargs.get('sub_container_type'),
                              insurance_cost=kwargs.get('insurance_cost'))
