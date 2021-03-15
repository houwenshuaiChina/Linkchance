CREATE TABLE [dbo].[AA_Department_Ext] (
  [departmentcode_lev1] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentname_lev1] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentcode_lev2] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentname_lev2] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentcode_lev3] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentname_lev3] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentcode_lev4] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentname_lev4] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentcode_lev5] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentname_lev5] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentcode_lev6] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentname_lev6] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentcode_lev7] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentname_lev7] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentcode_lev8] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentname_lev8] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentcode_lev9] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentname_lev9] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentcode_lev10] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentname_lev10] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentcode_lev11] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentname_lev11] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentcode_lev12] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentname_lev12] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentcode_lev13] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentname_lev13] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentcode_lev14] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentname_lev14] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentcode_lev15] nvarchar(32) COLLATE Chinese_PRC_CI_AS  NULL,
  [departmentname_lev15] nvarchar(200) COLLATE Chinese_PRC_CI_AS  NULL,
  [depth] nvarchar(10) COLLATE Chinese_PRC_CI_AS  NULL,
  [ts] timestamp  NULL,
  [departmentid_lev1] int  NULL,
  [departmentid_lev10] int  NULL,
  [departmentid_lev11] int  NULL,
  [departmentid_lev12] int  NULL,
  [departmentid_lev13] int  NULL,
  [departmentid_lev14] int  NULL,
  [departmentid_lev15] int  NULL,
  [departmentid_lev2] int  NULL,
  [departmentid_lev3] int  NULL,
  [departmentid_lev4] int  NULL,
  [departmentid_lev5] int  NULL,
  [departmentid_lev6] int  NULL,
  [departmentid_lev7] int  NULL,
  [departmentid_lev8] int  NULL,
  [departmentid_lev9] int  NULL,
  [id] int  NULL,
  [createTime] datetime  NULL
)
ON [PRIMARY]
GO

ALTER TABLE [dbo].[AA_Department_Ext] SET (LOCK_ESCALATION = TABLE)
GO

CREATE CLUSTERED INDEX [i_AA_Department_Ext_cluster]
ON [dbo].[AA_Department_Ext] (
  [createTime] ASC
)
WITH (
  FILLFACTOR = 90
)
FILESTREAM_ON [NULL]