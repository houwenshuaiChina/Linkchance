CREATE TABLE [dbo].[AA_Person] (
  [code] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [name] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [shorthand] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [nativePlace] nvarchar(30) COLLATE Chinese_PRC_CI_AS  NULL,
  [identityNo] nvarchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [familyPhoneNo] nvarchar(100) COLLATE Chinese_PRC_CI_AS  NULL,
  [officePhoneNo] nvarchar(100) COLLATE Chinese_PRC_CI_AS  NULL,
  [mobilePhoneNo] nvarchar(20) COLLATE Chinese_PRC_CI_AS  NULL,
  [emailAddr] nvarchar(100) COLLATE Chinese_PRC_CI_AS  NULL,
  [qqcode] nvarchar(30) COLLATE Chinese_PRC_CI_AS  NULL,
  [msnAddr] nvarchar(30) COLLATE Chinese_PRC_CI_AS  NULL,
  [uuNo] nvarchar(30) COLLATE Chinese_PRC_CI_AS  NULL,
  [postCode] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [postAddr] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [isSalesman] tinyint  NULL,
  [creditDate] decimal(28,14)  NULL,
  [creditQuantity] decimal(28,14)  NULL,
  [aRBalance_Abandon] decimal(28,14)  NULL,
  [aPBalance_Abandon] decimal(28,14)  NULL,
  [disabled] tinyint  NULL,
  [ts] timestamp  NULL,
  [updatedBy] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [priuserdefnvc1] nvarchar(500) COLLATE Chinese_PRC_CI_AS  NULL,
  [priuserdefdecm1] decimal(28,14)  NULL,
  [priuserdefnvc2] nvarchar(500) COLLATE Chinese_PRC_CI_AS  NULL,
  [priuserdefdecm2] decimal(28,14)  NULL,
  [priuserdefnvc3] nvarchar(500) COLLATE Chinese_PRC_CI_AS  NULL,
  [priuserdefdecm3] decimal(28,14)  NULL,
  [priuserdefnvc4] nvarchar(500) COLLATE Chinese_PRC_CI_AS  NULL,
  [priuserdefdecm4] decimal(28,14)  NULL,
  [priuserdefnvc5] nvarchar(500) COLLATE Chinese_PRC_CI_AS  NULL,
  [priuserdefdecm5] decimal(28,14)  NULL,
  [IsNavigator] tinyint  NULL,
  [IsOperator] tinyint  NULL,
  [id] int  IDENTITY(1,1) NOT NULL,
  [iddepartment] int  NULL,
  [idMarketingOrgan] int  NULL,
  [education] int  NULL,
  [gender] int  NULL,
  [identificationType] int  NULL,
  [position] int  NULL,
  [birthday] datetime  NULL,
  [madeDate] datetime  NULL,
  [updated] datetime  NULL,
  [createdTime] datetime  NULL,
  [VisitManage] tinyint DEFAULT 0 NULL,
  [autoCreateOperator] bit DEFAULT 0 NOT NULL,
  [personUserType] int  NULL,
  [idUserGroup] int  NULL,
  [AccountBank] int  NULL,
  [PositionTitle] int  NULL,
  [EmployeeCategory] int  NULL,
  [BankAccountNo] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [LeaveDate] datetime  NULL,
  [EnableSalaryPassword] int  NULL,
  [SalaryPassword] nvarchar(50) COLLATE Chinese_PRC_CI_AS  NULL,
  [EntryDate] datetime  NULL
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[AA_Person] SET (LOCK_ESCALATION = TABLE)
GO

CREATE NONCLUSTERED INDEX [IDX_AA_Person_cluster]
ON [dbo].[AA_Person] (
  [code] ASC
)
WITH (
  FILLFACTOR = 90
)
GO

CREATE NONCLUSTERED INDEX [IDX_AA_Person_iddepartment]
ON [dbo].[AA_Person] (
  [iddepartment] ASC
)
WITH (
  FILLFACTOR = 90
)
GO

CREATE NONCLUSTERED INDEX [Idx_AA_Person_MarketingOrgan]
ON [dbo].[AA_Person] (
  [idMarketingOrgan] ASC
)
WITH (
  FILLFACTOR = 90
)
GO

CREATE NONCLUSTERED INDEX [IDX_AA_Person_NAME]
ON [dbo].[AA_Person] (
  [name] ASC
)
WITH (
  FILLFACTOR = 90
)
GO

CREATE UNIQUE NONCLUSTERED INDEX [IDX_AA_Person_ID]
ON [dbo].[AA_Person] (
  [id] ASC
)
WITH (
  FILLFACTOR = 90
)