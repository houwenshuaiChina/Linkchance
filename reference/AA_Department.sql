CREATE TABLE [dbo].[AA_Department] (
  [code] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [name] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [isEndNode] tinyint  NULL,
  [depth] tinyint  NULL,
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
  [inId] nvarchar(560) COLLATE Chinese_PRC_CI_AS  NULL,
  [id] int  IDENTITY(1,1) NOT NULL,
  [idparent] int  NULL,
  [idMarketingOrgan] int  NULL,
  [iddirector] int  NULL,
  [madeDate] datetime  NULL,
  [updated] datetime  NULL,
  [createdTime] datetime  NULL
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[AA_Department] SET (LOCK_ESCALATION = TABLE)
GO

CREATE CLUSTERED INDEX [i_AA_Department_cluster]
ON [dbo].[AA_Department] (
  [code] ASC
)
WITH (
  FILLFACTOR = 90
)
FILESTREAM_ON [NULL]
GO

CREATE UNIQUE NONCLUSTERED INDEX [ix_AA_Department_ID]
ON [dbo].[AA_Department] (
  [id] ASC
)
WITH (
  FILLFACTOR = 90
)
GO

CREATE NONCLUSTERED INDEX [IDX_AA_Department_iddirector]
ON [dbo].[AA_Department] (
  [iddirector] ASC
)
WITH (
  FILLFACTOR = 90
)
GO

CREATE NONCLUSTERED INDEX [ix_AA_Department_2]
ON [dbo].[AA_Department] (
  [name] ASC
)
WITH (
  FILLFACTOR = 90
)
GO

CREATE NONCLUSTERED INDEX [IDX_AA_Department_idparent]
ON [dbo].[AA_Department] (
  [idparent] ASC
)
WITH (
  FILLFACTOR = 90
)
GO

CREATE NONCLUSTERED INDEX [Idx_AA_Department_MarketingOrgan]
ON [dbo].[AA_Department] (
  [idMarketingOrgan] ASC
)
WITH (
  FILLFACTOR = 90
)