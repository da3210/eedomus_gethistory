CREATE TABLE [dbo].[devices](
	[periph_id] [nvarchar](50) NOT NULL,
	[name] [nvarchar](100) NULL,
	[keep_history] [bit] NULL,
 CONSTRAINT [PK_devices2] PRIMARY KEY CLUSTERED 
(
	[periph_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]


CREATE TABLE [dbo].[History](
	[periph_id] [nvarchar](50) NOT NULL,
	[date] [datetime] NOT NULL,
	[value] [nvarchar](50) NULL,
 CONSTRAINT [PK_History] PRIMARY KEY CLUSTERED 
(
	[periph_id] ASC,
	[date] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO


CREATE VIEW [dbo].[v_Grafana]
AS
SELECT        dbo.History.date AS time, CASE WHEN ISNUMERIC(value) = 1 THEN CONVERT(float, value) ELSE NULL END AS Value, dbo.devices.name
FROM            dbo.History INNER JOIN
                         dbo.devices ON dbo.History.periph_id = dbo.devices.periph_id
GO
